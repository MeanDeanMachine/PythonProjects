from database import db
from bson import ObjectId
import bcrypt
from datetime import datetime

class User:
    def __init__(self):
        self.collection = db.users
    
    def create_user(self, email, password, name):
        # Check if user already exists
        if self.collection.find_one({"email": email}):
            return None
        
        # Hash password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        user_data = {
            "email": email,
            "password": hashed_password,
            "name": name,
            "watchlist": [],
            "favorites": [],
            "created_at": datetime.utcnow(),
            "profile_picture": None
        }
        
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)
    
    def authenticate_user(self, email, password):
        user = self.collection.find_one({"email": email})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            user['_id'] = str(user['_id'])
            return user
        return None
    
    def get_user_by_id(self, user_id):
        try:
            user = self.collection.find_one({"_id": ObjectId(user_id)})
            if user:
                user['_id'] = str(user['_id'])
                return user
        except:
            pass
        return None
    
    def add_to_watchlist(self, user_id, movie_id):
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$addToSet": {"watchlist": movie_id}}
            )
            return result.modified_count > 0
        except:
            return False
    
    def remove_from_watchlist(self, user_id, movie_id):
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"watchlist": movie_id}}
            )
            return result.modified_count > 0
        except:
            return False
    
    def get_watchlist(self, user_id):
        try:
            user = self.collection.find_one({"_id": ObjectId(user_id)})
            return user.get('watchlist', []) if user else []
        except:
            return []
