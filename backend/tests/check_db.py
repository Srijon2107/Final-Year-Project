import os
from pymongo import MongoClient
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Get URI
uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/fir_automation')

print(f"Attempting to connect to: {uri}")

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    # Force a connection check
    client.admin.command('ping')
    print("SUCCESS: Connected to MongoDB!")
    sys.exit(0)
except Exception as e:
    print(f"FAILURE: Could not connect to MongoDB.\nError: {e}")
    sys.exit(1)
