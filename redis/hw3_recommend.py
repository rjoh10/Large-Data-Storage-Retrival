from hw3_api import GraphAPI

# Create an instance of the GraphAPI class
api = GraphAPI()

# Rebuild the person/friend/book graph programmatically
api.add_node('Emily', 'Person')
api.add_node('Spencer', 'Person')
api.add_node('Cosmos', 'Book')
api.add_edge('Spencer', 'Emily', 'knows')
api.add_edge('Emily', 'Spencer', 'knows')
api.add_edge('Emily', 'Cosmos', 'bought')

# Add a new person
api.add_node('Jacob', 'Person')

# Add a new book
api.add_node('The Alchemist', 'Book')

# Connect Jacob to Spencer and Emily
api.add_edge('Jacob', 'Spencer', 'knows')
api.add_edge('Jacob', 'Emily', 'knows')

# Add some books that Jacob has bought
api.add_edge('Jacob', 'The Alchemist', 'bought')
api.add_edge('Jacob', 'Cosmos', 'bought')

# Get book recommendations for Spencer with a single API call
recommendations_for_spencer = api.get_recommendations('Spencer')
print("Recommendations for Spencer:", recommendations_for_spencer)