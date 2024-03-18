import redis

# Initialize Redis connection
db = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Remove the member from the set
db.srem('Spencer:edges', 'Cosmos')

# Remove the field from the hash
db.hdel('Spencer:edge_types', 'Cosmos')
