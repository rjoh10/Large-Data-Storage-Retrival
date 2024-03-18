from pymongo import MongoClient
from pymongo import DESCENDING

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['earthquake_db']
collection = db['earthquake_collection']

# Question 1: How many earthquakes occurred in the past hour?
query_1 = collection.count_documents({})
print("Question 1: How many earthquakes occurred in the past hour?")
print("Mongo Query:", query_1)

# Question 2: What are the details of earthquakes with magnitude greater than 2.5?
query_2 = collection.find({"properties.mag": {"$gt": 2.5}})
print("\nQuestion 2: What are the details of earthquakes with magnitude greater than 2.5?")
for quake in query_2.limit(5):  # Limiting to the first 5 results
    print(quake)


# Question 3: List earthquakes in California (place contains 'CA')
query_3 = collection.find({"properties.place": {"$regex": "CA"}})
print("\nQuestion 3: List earthquakes in California (place contains 'CA')")
for quake in query_3[:5]:
    print(quake)

# Question 4: What are the magnitudes of earthquakes in Hawaii?
query_4 = collection.find({"properties.place": {"$regex": "Hawaii"}}, {"properties.mag": 1})
print("\nQuestion 4: What are the magnitudes of earthquakes in Hawaii?")
for quake in query_4[:5]:
    print(quake)

# Question 5: Find earthquakes with a magnitude between 1.0 and 2.0
query_5 = collection.find({"properties.mag": {"$gte": 1.0, "$lte": 2.0}})
print("\nQuestion 5: Find earthquakes with a magnitude between 1.0 and 2.0")
for quake in query_5[:5]:
    print(quake)

# Question 6: List earthquakes ordered by magnitude in descending order
query_6 = collection.find().sort("properties.mag", -1)
print("\nQuestion 6: List earthquakes ordered by magnitude in descending order")
for quake in query_6[:5]:  # Limiting to the first 5 results
    print(quake)

# Question 7: Find the latest earthquake in the dataset
query_7 = collection.find().sort("properties.time", -1).limit(1)
print("\nQuestion 7: Find the latest earthquake in the dataset")
for quake in query_7:
    print(quake)

# Question 8: Find earthquakes with a tsunami alert
query_8 = collection.find({"properties.tsunami": 1})
print("\nQuestion 8: Find earthquakes with a tsunami alert")
for quake in query_8[:5]:  # Limiting to the first 5 results
    print(quake)

# Question 9: Count earthquakes with a magnitude greater than 3.0
query_9 = collection.count_documents({"properties.mag": {"$gt": 3.0}})
print("\nQuestion 9: Count earthquakes with a magnitude greater than 3.0")
print("Count:", query_9)

# Question 10: Find earthquakes with no alert status
query_10 = collection.find({"properties.alert": None})
print("\nQuestion 10: Find earthquakes with no alert status")
for quake in query_10[:5]:  # Limiting to the first 5 results
    print(quake)

# Close MongoDB connection
client.close()
