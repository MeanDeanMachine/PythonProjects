from database import db
from bson import ObjectId
from datetime import datetime

class Movie:
    def __init__(self):
        self.collection = db.movies
    
    def create_movie(self, title, description, genre, year, duration, video_url, thumbnail_url, rating=0):
        movie_data = {
            "title": title,
            "description": description,
            "genre": genre,
            "year": year,
            "duration": duration,
            "video_url": video_url,
            "thumbnail_url": thumbnail_url,
            "rating": rating,
            "views": 0,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        
        result = self.collection.insert_one(movie_data)
        return str(result.inserted_id)
    
    def get_all_movies(self, limit=50, skip=0):
        movies = list(self.collection.find().skip(skip).limit(limit))
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        return movies
    
    def get_movie_by_id(self, movie_id):
        try:
            movie = self.collection.find_one({"_id": ObjectId(movie_id)})
            if movie:
                movie['_id'] = str(movie['_id'])
                return movie
        except:
            pass
        return None
    
    def search_movies(self, query, limit=20):
        search_filter = {
            "$or": [
                {"title": {"$regex": query, "$options": "i"}},
                {"description": {"$regex": query, "$options": "i"}},
                {"genre": {"$regex": query, "$options": "i"}}
            ]
        }
        
        movies = list(self.collection.find(search_filter).limit(limit))
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        return movies
    
    def get_movies_by_genre(self, genre, limit=20):
        movies = list(self.collection.find({"genre": {"$regex": genre, "$options": "i"}}).limit(limit))
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        return movies
    
    def increment_views(self, movie_id):
        try:
            self.collection.update_one(
                {"_id": ObjectId(movie_id)},
                {"$inc": {"views": 1}}
            )
            return True
        except:
            return False
    
    def get_trending_movies(self, limit=10):
        movies = list(self.collection.find().sort("views", -1).limit(limit))
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        return movies
