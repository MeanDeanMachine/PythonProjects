from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User

auth_bp = Blueprint('auth', __name__)
user_model = User()

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        if not email or not password or not name:
            return jsonify({'error': 'Email, password, and name are required'}), 400
        
        user_id = user_model.create_user(email, password, name)
        
        if not user_id:
            return jsonify({'error': 'User already exists'}), 409
        
        access_token = create_access_token(identity=user_id)
        
        return jsonify({
            'message': 'User created successfully',
            'access_token': access_token,
            'user_id': user_id
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        user = user_model.authenticate_user(email, password)
        
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        access_token = create_access_token(identity=user['_id'])
        
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user': {
                'id': user['_id'],
                'email': user['email'],
                'name': user['name']
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    try:
        user_id = get_jwt_identity()
        user = user_model.get_user_by_id(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'user': {
                'id': user['_id'],
                'email': user['email'],
                'name': user['name'],
                'watchlist': user.get('watchlist', []),
                'favorites': user.get('favorites', [])
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
