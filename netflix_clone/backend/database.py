from pymongo import MongoClient
from config import Config
import logging

class Database:
    _instance = None
    _client = None
    _db = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def connect(self):
        try:
            self._client = MongoClient(Config.MONGODB_URI)
            self._db = self._client.get_database()
            # Test connection
            self._client.admin.command('ping')
            logging.info("Connected to MongoDB successfully")
            return True
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")
            return False
    
    def get_db(self):
        if self._db is None:
            self.connect()
        return self._db
    
    def close_connection(self):
        if self._client:
            self._client.close()

# Initialize database instance
db_instance = Database()
db = db_instance.get_db()
