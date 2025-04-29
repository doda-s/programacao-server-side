import os

# Caminho relativo para a aplicação
application_absolute_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    # Busca um arquivo na estrutura de arquivos contendo a chave secreta
    # Utilizamos 'you-will-never-guess' para ambiente de desenvolvimento
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess.'
    
    # Endereço para o banco de dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(application_absolute_dir, 'app.db'))
    
    # Ativa ou desativa log das modificações
    SQLALCHEMY_TRACK_MODIFICATIONS = False