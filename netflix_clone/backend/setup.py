#!/usr/bin/env python3
"""
Setup script for Netflix Clone Backend
This script sets up the environment and seeds the database with sample data.
"""

import os
import sys
import subprocess
from database import db_instance
from seed_data import seed_movies

def install_dependencies():
    """Install Python dependencies"""
    print("Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install dependencies: {e}")
        return False

def setup_environment():
    """Setup environment variables"""
    if not os.path.exists('.env'):
        print("Creating .env file...")
        with open('.env', 'w') as f:
            f.write("MONGODB_URI=mongodb://localhost:27017/netflix_clone\n")
            f.write("JWT_SECRET_KEY=your-super-secret-jwt-key-change-this-in-production\n")
            f.write("FLASK_ENV=development\n")
            f.write("PORT=5000\n")
        print("✓ Environment file created")
    else:
        print("✓ Environment file already exists")

def setup_database():
    """Setup database connection and seed data"""
    print("Setting up database...")
    
    if not db_instance.connect():
        print("✗ Failed to connect to MongoDB")
        print("Please ensure MongoDB is running on your system")
        return False
    
    print("✓ Connected to MongoDB")
    
    # Seed sample data
    print("Seeding sample movie data...")
    if seed_movies():
        print("✓ Sample data seeded successfully")
    else:
        print("✗ Failed to seed sample data")
    
    return True

def main():
    print("🎬 Netflix Clone Backend Setup")
    print("=" * 40)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup environment
    setup_environment()
    
    # Setup database
    if not setup_database():
        print("\n⚠️  Database setup failed. You can run the app, but you'll need to:")
        print("1. Install and start MongoDB")
        print("2. Run 'python seed_data.py' to add sample movies")
    
    print("\n🚀 Setup complete!")
    print("Run 'python app.py' to start the server")

if __name__ == "__main__":
    main()
