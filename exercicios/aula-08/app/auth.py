import datetime
import jwt

from functools import wraps
from flask import request, jsonify, Blueprint, current_app

auth_blueprint = Blueprint('auth', __name__)

# Rota de autenticação
@auth_blueprint.route('/login', methods=['POST'])
def login():
    # Pega o payload em json
    auth_data = request.get_json()
    
    # Extrai os dados do payload
    username = auth_data.get('username')
    password = auth_data.get('password')
    
    if username == 'admin' and password == 'pass':
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
        current_app.config["SECRET_KEY"],
        algorithm='HS256'
        )
        return jsonify({'token': token}), 200
    
    return jsonify({'message': 'Invalid username or passowrd.'}), 401

def token_required(f):
    
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']    
        
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401
        
        try:
            data= jwt.decode(token, current_app.config['SECRET_KEY'], algorithms='HS256')
            current_user = data['user']
            
        except jwt.ExpiredSignatureError:   
            return jsonify({'message': 'Token has expired.'}), 401
        
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid.'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated