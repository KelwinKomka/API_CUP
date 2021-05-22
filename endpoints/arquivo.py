from flask import Blueprint, jsonify, request

from arquivo.info import montar_arquivo_info
from arquivo.ddl import montar_arquivo_ddl
from arquivo.estrutura_conf import montar_arquivo_estrutura_conf

arquivo_bp = Blueprint('arquivo', __name__)

@arquivo_bp.route('/info', methods=['GET'])
def get_info_file():
    versao = request.args.get('versao')
    banco = request.args.get('banco')

    return montar_arquivo_info(versao, banco)

@arquivo_bp.route('/ddl', methods=['GET'])
def get_ddl_file():
    versao = request.args.get('versao')
    banco = request.args.get('banco')

    return montar_arquivo_ddl(versao, banco)

@arquivo_bp.route('/estruturas_conf', methods=['GET'])
def get_estrutura_file():
    versao = request.args.get('versao')
    banco = request.args.get('banco')

    return montar_arquivo_estrutura_conf(versao, banco)