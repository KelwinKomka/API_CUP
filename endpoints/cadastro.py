from dao.item_versao_dao import inserir_item_versao
from flask import Blueprint, request, jsonify, abort
from datetime import date

from models.script import Script
from models.item_versao import Item_Versao
from models.versao import Versao

from dao.script_dao import inserir_script
import dao.versao_dao
from dao.tipo_script_dao import buscar_tipo_script_by_desc
from dao.dev_dao import buscar_dev

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
    versao.data = today
    versao.dev = request.json.get('desenvolvimento', 'T')
    versao.prod = request.json.get('producao', 'F')
    versao.habilitada = request.json.get('habilitada', 'T')

    retorno = dao.versao_dao.inserir_versao(versao)
    if "ok" == retorno:
        retorno = 'Registro de versão adicionado.'
    else:
        retorno = 'Erro ao inserir registro: ' + retorno

    return resposta(retorno)

@cadastro_bp.route('/item_versao', methods=['POST'])
def criar_item_versao():
    if not request.json:
        abort(400)

    valor_versao = request.json['versao']
    login_dev = request.json['usuario']

    versao = dao.versao_dao.buscar_versao(valor_versao)
    if not versao:
        return resposta('Versão '+valor_versao+' não encontrada!')
    
    dev = buscar_dev(login_dev)
    if not dev:
        return resposta('Desenvolvedor '+login_dev+' não encontrado!')
        
    today = date.today()

    item_versao = Item_Versao()
    item_versao.versao_id = versao.versao_id
    item_versao.dev_id = dev.dev_id
    item_versao.dev = request.json['usuario']
    item_versao.ticket = request.json['ticket']
    item_versao.projeto = request.json['projeto']
    item_versao.modulo = request.json['modulo']
    item_versao.aplicacao = request.json['aplicacao']
    item_versao.release = request.json['release']
    item_versao.descricao = request.json.get('descricao', '')
    item_versao.ticket = request.json.get('teste', '')
    item_versao.data = today
    
    retorno = inserir_item_versao(item_versao)
    if "ok" == retorno:
        retorno = 'Registro de item da versão adicionado.'
    else:
        retorno = 'Erro ao inserir registro: ' + retorno

    return resposta(retorno)

@cadastro_bp.route('/script', methods=['POST'])
def criar_script():
    if not request.json:
        abort(400)

    valor_versao = request.json['versao']
    valor_tipo_script = request.json['tipo_script']

    versao = dao.versao_dao.buscar_versao(valor_versao)
    if not versao:
        return resposta('Versão '+valor_versao+' não encontrada!')

    tipo_script = buscar_tipo_script_by_desc(valor_tipo_script)
    if not tipo_script:
        return resposta('Tipo de script '+valor_tipo_script+' não encontrado!')
    
    script = Script()
    script.versao_id = versao.versao_id
    script.tipo_script_id = tipo_script.tipo_script_id
    script.tipo_script = valor_tipo_script
    script.descricao = request.json['descricao']
    script.codigo = request.json['codigo']
    script.skip = request.json.get('skip', 'F')
    script.tipo_banco = request.json['tipo_banco']
    script.old_codigo = request.json.get('old_codigo', '')
    script.banco = request.json['banco']
    
    retorno = inserir_script(script)
    if "ok" == retorno:
        retorno = 'Registro de script adicionado.'
    else:
        retorno = 'Erro ao inserir registro: ' + retorno

    return resposta(retorno)

def resposta(msg):
    return jsonify({'resposta': msg}), 201