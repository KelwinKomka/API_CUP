from models.script import Script
from models.item_versao import Item_Versao
from models.versao import Versao
from flask import Blueprint, request, jsonify, abort
from datetime import date

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/versao', methods=['POST'])
def criar_versao():
    if not request.json:
        abort(400)

    today = date.today()

    versao = Versao()
    versao.major = request.json['major']
    versao.minor = request.json['minor']
    versao.banco = request.json['banco']
    versao.data = today.strftime("%d/%m/%Y")
    versao.dev = request.json.get('desenvolvimento', 'T')
    versao.prod = request.json.get('producao', 'F')
    versao.habilitada = request.json.get('habilitada', 'T')

    # inserir no banco

    return resposta('Registro da versão adicionado.')

@cadastro_bp.route('/item_versao', methods=['POST'])
def criar_item_versao():
    if not request.json:
        abort(400)
        
    today = date.today()

    item_versao = Item_Versao()
    item_versao.usuario = request.json['usuario']
    item_versao.ticket = request.json['ticket']
    item_versao.projeto = request.json['projeto']
    item_versao.modulo = request.json['modulo']
    item_versao.aplicacao = request.json['aplicacao']
    item_versao.release = request.json['release']
    item_versao.descricao = request.json.get('descricao', '')
    item_versao.ticket = request.json.get('teste', '')
    item_versao.data = today.strftime("%d/%m/%Y")
    # inserir no banco

    return resposta('Registro de item da versão adicionado.')

@cadastro_bp.route('/script', methods=['POST'])
def criar_script():
    if not request.json:
        abort(400)

    script = Script()
    script.tipo_script = request.json['tipo_script']
    script.descricao = request.json['descricao']
    script.codigo = request.json['codigo']
    script.skip = request.json.get('skip', 'F')
    script.tipo_banco = request.json['tipo_banco']
    script.old_codigo = request.json.get('old_codigo', '')
    script.banco = request.json['banco']
    # inserir no banco

    return resposta('Registro de item da versão adicionado.')

def resposta(msg):
    return jsonify({'resposta': msg}), 201