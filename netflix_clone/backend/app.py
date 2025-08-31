from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from database import db_instance
from routes.auth import auth_bp
from routes.movies import movies_bp
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize extensions with proper CORS configuration
    CORS(app, 
         origins=['http://localhost:3000', 'http://127.0.0.1:3000'],
         methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
         allow_headers=['Content-Type', 'Authorization'],
         supports_credentials=True)
    jwt = JWTManager(app)
    
    # Connect to database
    if not db_instance.connect():
        logging.error("Failed to connect to database")
        return None
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(movies_bp, url_prefix='/api/movies')
    
    # Health check endpoint
    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'healthy', 'message': 'Netflix Clone API is running'}), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({'error': 'Token has expired'}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'error': 'Invalid token'}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'error': 'Authorization token is required'}), 401
    
    return app

if __name__ == '__main__':
    app = create_app()
    if app:
        app.run(host='0.0.0.0', port=Config.PORT, debug=Config.FLASK_ENV == 'development')
    else:
        logging.error("Failed to create Flask application")
