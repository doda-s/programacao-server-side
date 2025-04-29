from flask import Blueprint

blueprint = Blueprint('main', __name__)

# Encapsular rotas
from app.routes import clients