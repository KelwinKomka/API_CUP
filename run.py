from flask import Flask, jsonify, make_response
import configparser

from endpoints.cadastro import cadastro_bp
from endpoints.arquivo import arquivo_bp

from db import connect_db

app = Flask(__name__)

app.register_blueprint(cadastro_bp, url_prefix='/cadastro')
app.register_blueprint(arquivo_bp, url_prefix='/arquivo')

config = configparser.ConfigParser()
config.read('config.ini')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'resposta': 'Não encontrado!'}), 404)
    
if __name__ == '__main__':
    # connect_db(config)
    app.run(host='0.0.0.0', port=5000)