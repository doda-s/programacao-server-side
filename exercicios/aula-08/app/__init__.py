from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from app.data_base import data_base
from app.auth import auth_blueprint, token_required

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Application secret key
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    data_base.init_app(app)
    migrate.init_app(app, data_base)

    from app.routes import routes_blueprint as routes_blueprint
    app.register_blueprint(routes_blueprint)
    
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'message': 'Bad request.'}), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({'message': 'Unauthorized'}), 401
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': 'Not found.'}), 404
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({'message': 'Internal server error.'}), 500
    
    @app.errorhandler(503)
    def service_unavaliable(error):
        return jsonify({'message': 'Service unavaliable.'})
    
    return app