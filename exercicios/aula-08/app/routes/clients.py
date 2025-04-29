from flask import jsonify, request
from app import data_base
from app.models import Client
from app.routes import blueprint
from app.auth import token_required

@blueprint.route('/clients', methods=['GET'])
@token_required
def get_clients(current_user):
    
    current_id = request.args.get('client_id')
    
    if client_id:
        try:
            client = Client.query.get_or_404(client_id)
            return jsonify(client.to_dict()), 200
        except Exception as e:
            return jsonify({'error': str(e)})

    else:
        try:
            client = Client.query.all()
            return jsonify([client.to_dict() for client in clients]), 200
        
        except Exception as e:
            return jsonify({'error': str(e)})
