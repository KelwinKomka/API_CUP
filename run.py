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

@app.route('/index')
def get_index():
    return ''' <!DOCTYPE html>
<html>
    <body>
        <h1>Chamadas:</h1>
        <p>/arquivo/info</p>
        <p>/arquivo/ddl</p>
        <p>/arquivo/estruturas_conf</p>
        <br/>
        <p>/cadastro/versao</p>
        <p>/cadastro/item_versao</p>
        <p>/cadastro/script</p>
    </body>
</html>'''
    
if __name__ == '__main__':
    # connect_db(config)
    app.run(host='0.0.0.0', port=5000)