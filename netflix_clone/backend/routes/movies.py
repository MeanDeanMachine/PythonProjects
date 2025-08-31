from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.movie import Movie
from models.user import User

movies_bp = Blueprint('movies', __name__)
movie_model = Movie()
user_model = User()

@movies_bp.route('/', methods=['GET'])
def get_movies():
    try:
        limit = int(request.args.get('limit', 50))
        skip = int(request.args.get('skip', 0))
        
        movies = movie_model.get_all_movies(limit=limit, skip=skip)
        
        return jsonify({
            'movies': movies,
            'count': len(movies)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@movies_bp.route('/<movie_id>', methods=['GET'])
def get_movie(movie_id):
    try:
        movie = movie_model.get_movie_by_id(movie_id)
        
        if not movie:
            return jsonify({'error': 'Movie not found'}), 404
        
        return jsonify({'movie': movie}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@movies_bp.route('/search', methods=['GET'])
def search_movies():
    try:
        query = request.args.get('q', '')
        limit = int(request.args.get('limit', 20))
        
        if not query:
            return jsonify({'error': 'Search query is required'}), 400
        
        movies = movie_model.search_movies(query, limit=limit)
        
        return jsonify({
            'movies': movies,
            'count': len(movies),
            'query': query
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@movies_bp.route('/genre/<genre>', methods=['GET'])
def get_movies_by_genre(genre):
    try:
        limit = int(request.args.get('limit', 20))
        movies = movie_model.get_movies_by_genre(genre, limit=limit)
        
        return jsonify({
            'movies': movies,
            'count': len(movies),
            'genre': genre
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@movies_bp.route('/trending', methods=['GET'])
def get_trending_movies():
    try:
        limit = int(request.args.get('limit', 10))
        movies = movie_model.get_trending_movies(limit=limit)
        
        return jsonify({
            'movies': movies,
            'count': len(movies)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@movies_bp.route('/<movie_id>/watch', methods=['POST'])
@jwt_required()
def watch_movie(movie_id):
    try:
        movie = movie_model.get_movie_by_id(movie_id)
        
        if not movie:
            return jsonify({'error': 'Movie not found'}), 404
        
        # Increment view count
        movie_model.increment_views(movie_id)
        
        return jsonify({
            'message': 'Movie accessed successfully',
            'video_url': movie['video_url']
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@movies_bp.route('/<movie_id>/watchlist', methods=['POST'])
@jwt_required()
def add_to_watchlist(movie_id):
    try:
        user_id = get_jwt_identity()
        
        # Check if movie exists
        movie = movie_model.get_movie_by_id(movie_id)
        if not movie:
            return jsonify({'error': 'Movie not found'}), 404
        
        success = user_model.add_to_watchlist(user_id, movie_id)
        
        if success:
            return jsonify({'message': 'Movie added to watchlist'}), 200
        else:
            return jsonify({'error': 'Failed to add movie to watchlist'}), 500
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@movies_bp.route('/<movie_id>/watchlist', methods=['DELETE'])
@jwt_required()
def remove_from_watchlist(movie_id):
    try:
        user_id = get_jwt_identity()
        
        success = user_model.remove_from_watchlist(user_id, movie_id)
        
        if success:
            return jsonify({'message': 'Movie removed from watchlist'}), 200
        else:
            return jsonify({'error': 'Failed to remove movie from watchlist'}), 500
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
