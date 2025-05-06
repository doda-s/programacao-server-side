from flask import jsonify, request
from app import data_base
from app.models import Client
from app.routes import routes_blueprint
from app.auth import token_required

@routes_blueprint.route('/clients', methods=['GET'])
@token_required
def get_clients(current_user):
    
    current_id = request.args.get('client_id')
    
    if current_id:
        try:
            client = Client.query.get_or_404(current_id)
            return jsonify(client.to_dict()), 200
        except Exception as e:
            return jsonify({'error': str(e)})

    else:
        try:
            clients = Client.query.all()
            return jsonify([client.to_dict() for client in clients]), 200
        
        except Exception as e:
            return jsonify({'error': str(e)})

@routes_blueprint.route('/clients', methods=['POST'])
@token_required
def create_client(current_user):
    try:
        data = request.get_json() or {}
        
        if 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email is required.'}), 400
        
        if Client.query.filter_by(name=data['name']).first():
            return jsonify({'error': 'Email already exist.'}), 400
        
        client = Client(name=data['name'], email=data['email'])
        data_base.session.add(client)
        data_base.session.commit()
        return jsonify(client.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500 # server error