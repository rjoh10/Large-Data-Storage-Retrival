import redis

class GraphAPI:
    def __init__(self, host='localhost', port=6379, db=0):
        self.db = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def add_node(self, name, node_type):
        self.db.hmset(name, {'type': node_type})

    def add_edge(self, name1, name2, edge_type):
        self.db.sadd(name1 + ':edges', name2)  # Use sadd to add to a set
        self.db.hset(name1 + ':edge_types', name2, edge_type)  # Store edge type in a separate hash

    def get_adjacent(self, name, node_type=None, edge_type=None):
        adjacent_nodes = self.db.smembers(name + ':edges')
        if node_type:
            adjacent_nodes = [node for node in adjacent_nodes if self.db.hget(node, 'type') == node_type]
        if edge_type:
            adjacent_edge_types = self.db.hgetall(name + ':edge_types')
            adjacent_nodes = [node for node in adjacent_nodes if adjacent_edge_types.get(node) == edge_type]
        return adjacent_nodes

    def get_recommendations(self, name):
        recommendations = set()
        person_books = self.get_adjacent(name, node_type='Book', edge_type='bought')

        friends = self.get_adjacent(name, node_type='Person', edge_type='knows')

        for friend in friends:
            friend_books = self.get_adjacent(friend, node_type='Book', edge_type='bought')
            recommendations.update(friend_books)

        return list(recommendations - set(person_books))