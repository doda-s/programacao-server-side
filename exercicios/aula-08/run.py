from app import create_app, data_base
from app.models import Client

# Cria o aplicativo
app = create_app()

@app.shell_context_processor
def make_shell_context():
    # Pode executar comandos shell durante a execução do app
    return {'data_base': data_base, 'Client': Client}