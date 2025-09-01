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
            "title": "Momo Wins the Masters",
            "description": "After Stephen becomes hospitalized due to a cheese allergy, one dog defies all the odds by picking up Bernie's old golf clubs to win the whole Masters.",
            "genre": "Comedy",
            "year": 2025,
            "duration": 136,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
            "thumbnail_url": "https://i.imgur.com/zpHjZe3.png",
            "rating": 8.7
        },
        {
            "title": "Happy Gilmore 3",
            "description": "After winning the PGA tournament, Happy Gilmore embarks on a new adventure.",
            "genre": "Action, Comedy, Sports",
            "year": 2025,
            "duration": 148,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_2mb.mp4",
            "thumbnail_url": "https://i.imgur.com/fzHOtkr.png",
            "rating": 8.8
        },
        {
            "title": "The Summer Piper broke up with Brodie",
            "description": "Young love, a story of a romance that fizzled out, keep your head up short king.",
            "genre": "Romance",
            "year": 2025,
            "duration": 154,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
            "thumbnail_url": "https://i.imgur.com/HdzlnkP.png",
            "rating": 8.9
        },
        {
            "title": "Seinfeld",
            "description": "The classic sitcom about four friends in New York City.",
            "genre": "Comedy",
            "year": 1990,
            "duration": 152,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_2mb.mp4",
            "thumbnail_url": "https://i.imgur.com/biVKvaG.jpeg",
            "rating": 9.0
        },
        {
            "title": "Pria meets the Lake Dolphin",
            "description": "A tale as old as time, one girl paddles out in Emerald Lake and discovers the hidden treasure of the lake, a lone dolphin.",
            "genre": "Drama",
            "year": 2025,
            "duration": 142,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_5mb.mp4",
            "thumbnail_url": "https://i.imgur.com/XtyeXhz.png",
            "rating": 9.3
        },
        {
            "title": "Lola does Returns",
            "description": "Strap yourselves in its going to be a long one, Lola does returns for her last Gucci run.",
            "genre": "Drama, Fantasy, Horror",
            "year": 2016,
            "duration": 50,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_5mb.mp4",
            "thumbnail_url": "https://i.imgur.com/Li4jcQQ.png",
            "rating": 8.7
        },
        {
            "title": "Mandy Goes on a Plane",
            "description": "What turns out to be a routine business trip takes an unexpected turn when Mandy discovers she has an annoying seat neighbor",
            "genre": "Crime, Drama, Thriller",
            "year": 2025,
            "duration": 47,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
            "thumbnail_url": "https://i.imgur.com/lulDdYi.png",
            "rating": 9.5
        },
        {
            "title": "The Dark Knight",
            "description": "After Batman's parents are murdered, he vows to rid Gotham of corruption as a vigilante.",
            "genre": "Action, Crime, Drama",
            "year": 2008,
            "duration": 58,
            "video_url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_2mb.mp4",
            "thumbnail_url": "https://i.imgur.com/75VcOVc.jpeg",
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
