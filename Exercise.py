from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create or access a database
db = client['example_database']

# Create or access a collection (similar to a table in relational databases)
collection = db['users']

# Create data (Insert)
user_data = [
    {"name": "ilechukwu mmeosoma", "age": 25},
    {"name": "opus pocus", "age": 30},
    {"name": "livid bun", "age": 20},
]
result = collection.insert_many(user_data)
print("Inserted IDs:", result.inserted_ids)

# Read data (Retrieve)
all_users = collection.find()
print("\nAll Users:")
for user in all_users:
    print(user)

# Update data
query = {"name": "ilechukwu mmeosoma"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)
print("\nUser 'ilechukwu mmeosoma' updated.")

# Modify data (Update)
query = {"name": "ilechukwu mmeosoma"}
new_values = {"$set": {"name": "ELijah Michaelson"}}
collection.update_one(query, new_values)
print("\nUser 'ilechukwu mmeosoma' modified to 'Johnathan Doe'.")

# Read data after modification
all_users_after_update = collection.find()
print("\nAll Users After Update:")
for user in all_users_after_update:
    print(user)

# Delete data   
query = {"name": "livid bun"}
collection.delete_one(query)
print("\nUser 'livid bun' deleted.")

# Read data after deletion
all_users_after_deletion = collection.find()
print("\nAll Users After Deletion:")
for user in all_users_after_deletion:
    print(user)