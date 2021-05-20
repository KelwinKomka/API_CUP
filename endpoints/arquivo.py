from flask import Blueprint, jsonify

arquivo_bp = Blueprint('arquivo', __name__)

@arquivo_bp.route('/info/<string:versao>', methods=['GET'])
def get_info_file(versao):
    return jsonify({'info': ''})

@arquivo_bp.route('/ddl/<string:versao>', methods=['GET'])
def geT_ddl_file(versao):
    return jsonify({'ddl': ''})

@arquivo_bp.route('/estruturas_conf/<string:versao>', methods=['GET'])
def get_estrutura_file(versao):
    return jsonify({'estruturas_conf': ''})