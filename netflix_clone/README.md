# Netflix Clone

A full-stack Netflix clone built with Python Flask backend, React frontend, and MongoDB database.

## Features

- User authentication and authorization
- Browse movies and TV shows
- Search functionality
- Video streaming
- Responsive Netflix-like UI
- User profiles and watchlists

## Tech Stack

- **Backend**: Python Flask, Flask-JWT-Extended, PyMongo
- **Frontend**: React, Axios, React Router
- **Database**: MongoDB
- **Authentication**: JWT tokens

## Prerequisites

- Python 3.8+
- Node.js 16+
- MongoDB (local installation or MongoDB Atlas)

## Quick Start

### 1. Backend Setup

```bash
cd backend
python setup.py
```

This will:
- Install all Python dependencies
- Create environment configuration
- Connect to MongoDB and seed sample data

### 2. Frontend Setup

```bash
cd frontend
setup.bat
```

This will install all Node.js dependencies.

### 3. Start the Application

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

### 4. Access the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Manual Setup (Alternative)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update MongoDB connection string and JWT secret

4. Seed sample data:
   ```bash
   python seed_data.py
   ```

5. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

### Database Setup

1. Install MongoDB locally or use MongoDB Atlas
2. Create a database named `netflix_clone`
3. The application will automatically create collections as needed

## API Endpoints

- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/movies` - Get all movies
- `GET /api/movies/search` - Search movies
- `GET /api/user/profile` - Get user profile
- `POST /api/user/watchlist` - Add to watchlist

## License

MIT License
