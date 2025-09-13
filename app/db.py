from pymongo import MongoClient
import sys

# The correct connection string for a local MongoDB without authentication
MONGO_URI = "mongodb://localhost:27017/"

try:
    client = MongoClient(MONGO_URI)
    db = client["assessment_db"]
    collection = db["employees"]
    print("Database connection successful.")

except Exception as e:
    print(f"Error connecting to MongoDB: {e}", file=sys.stderr)
    sys.exit(1)


employee_schema = {
    "bsonType": "object",
    "required": ["employee_id", "name", "department", "salary", "joining_date", "skills"],
    "properties": {
        "employee_id": {"bsonType": "string"},
        "name": {"bsonType": "string"},
        "department": {"bsonType": "string"},
        "salary": {"bsonType": ["int", "double"]},
        "joining_date": {"bsonType": "string"},
        "skills": {
            "bsonType": "array",
            "items": {"bsonType": "string"}
        }
    }
}

# Create the collection with validation if it doesn't exist
if "employees" not in db.list_collection_names():
    db.create_collection(
        "employees",
        validator={"$jsonSchema": employee_schema},
        validationLevel="strict"
    )
    print("Collection 'employees' created with schema validation.")

# Ensure unique index on employee_id
try:
    collection.create_index("employee_id", unique=True)
    print("Unique index created on 'employee_id'.")
except Exception as e:
    print(f"Error creating index: {e}", file=sys.stderr)
