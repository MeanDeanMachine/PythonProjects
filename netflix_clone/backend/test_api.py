#!/usr/bin/env python3
"""
Test script to verify the Netflix Clone backend is working
"""

import requests
import json
from database import db_instance
from models.movie import Movie

def test_database_connection():
    """Test MongoDB connection"""
    print("Testing database connection...")
    if db_instance.connect():
        print("✓ Database connected successfully")
        return True
    else:
        print("✗ Database connection failed")
        return False

def test_movie_seeding():
    """Test if movies exist in database"""
    print("Checking movies in database...")
    movie_model = Movie()
    movies = movie_model.get_all_movies(limit=100)
    
    if movies:
        print(f"✓ Found {len(movies)} movies in database")
        for movie in movies[:3]:
            print(f"  - {movie['title']} ({movie['year']})")
        return True
    else:
        print("✗ No movies found in database")
        return False

def seed_if_empty():
    """Seed database if no movies exist"""
    movie_model = Movie()
    movies = movie_model.get_all_movies(limit=1)
    
    if not movies:
        print("Database is empty. Seeding with sample data...")
        from seed_data import seed_movies
        if seed_movies():
            print("✓ Sample data seeded successfully")
            return True
        else:
            print("✗ Failed to seed sample data")
            return False
    return True

def test_api_endpoints():
    """Test API endpoints"""
    base_url = "http://localhost:5000/api"
    
    print("Testing API endpoints...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✓ Health endpoint working")
        else:
            print(f"✗ Health endpoint returned {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot connect to backend server: {e}")
        print("Make sure to run 'python app.py' first")
        return False
    
    # Test movies endpoint
    try:
        response = requests.get(f"{base_url}/movies", timeout=5)
        if response.status_code == 200:
            data = response.json()
            movie_count = len(data.get('movies', []))
            print(f"✓ Movies endpoint working - {movie_count} movies found")
            return True
        else:
            print(f"✗ Movies endpoint returned {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Movies endpoint error: {e}")
        return False

def main():
    print("🎬 Netflix Clone Backend Test")
    print("=" * 40)
    
    # Test database
    if not test_database_connection():
        print("\n❌ Database connection failed. Please install and start MongoDB.")
        return
    
    # Seed if needed
    if not seed_if_empty():
        print("\n❌ Failed to seed database.")
        return
    
    # Check movies
    if not test_movie_seeding():
        print("\n❌ No movies in database.")
        return
    
    # Test API (optional - only if server is running)
    print("\nTesting API endpoints (optional)...")
    test_api_endpoints()
    
    print("\n✅ Backend test complete!")
    print("If API tests failed, start the server with: python app.py")

if __name__ == "__main__":
    main()
