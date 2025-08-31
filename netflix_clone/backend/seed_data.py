from models.movie import Movie
from database import db_instance
import logging

def seed_movies():
    """Seed the database with sample movie data"""
    
    # Connect to database
    if not db_instance.connect():
        logging.error("Failed to connect to database")
        return False
    
    movie_model = Movie()
    
    sample_movies = [
        {
            "title": "The Matrix",
            "description": "A computer programmer discovers that reality as he knows it is a simulation controlled by machines.",
            "genre": "Action, Sci-Fi",
            "year": 1999,
            "duration": 136,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=The+Matrix",
            "rating": 8.7
        },
        {
            "title": "Inception",
            "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea.",
            "genre": "Action, Sci-Fi, Thriller",
            "year": 2010,
            "duration": 148,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_2mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=Inception",
            "rating": 8.8
        },
        {
            "title": "The Shawshank Redemption",
            "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "genre": "Drama",
            "year": 1994,
            "duration": 142,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_5mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=Shawshank",
            "rating": 9.3
        },
        {
            "title": "Pulp Fiction",
            "description": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.",
            "genre": "Crime, Drama",
            "year": 1994,
            "duration": 154,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=Pulp+Fiction",
            "rating": 8.9
        },
        {
            "title": "The Dark Knight",
            "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests.",
            "genre": "Action, Crime, Drama",
            "year": 2008,
            "duration": 152,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_2mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=Dark+Knight",
            "rating": 9.0
        },
        {
            "title": "Stranger Things",
            "description": "When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces.",
            "genre": "Drama, Fantasy, Horror",
            "year": 2016,
            "duration": 50,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_5mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=Stranger+Things",
            "rating": 8.7
        },
        {
            "title": "Breaking Bad",
            "description": "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine.",
            "genre": "Crime, Drama, Thriller",
            "year": 2008,
            "duration": 47,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=Breaking+Bad",
            "rating": 9.5
        },
        {
            "title": "The Crown",
            "description": "Follows the political rivalries and romance of Queen Elizabeth II's reign and the events that shaped the second half of the twentieth century.",
            "genre": "Biography, Drama, History",
            "year": 2016,
            "duration": 58,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_2mb.mp4",
            "thumbnail_url": "https://via.placeholder.com/300x450/000000/FFFFFF?text=The+Crown",
            "rating": 8.7
        }
    ]
    
    try:
        for movie_data in sample_movies:
            movie_id = movie_model.create_movie(**movie_data)
            if movie_id:
                logging.info(f"Created movie: {movie_data['title']} with ID: {movie_id}")
            else:
                logging.error(f"Failed to create movie: {movie_data['title']}")
        
        logging.info("Sample movie data seeded successfully")
        return True
        
    except Exception as e:
        logging.error(f"Error seeding movie data: {e}")
        return False

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    seed_movies()
