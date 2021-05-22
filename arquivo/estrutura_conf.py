from dao.script_dao import buscar_scripts
from flask import jsonify

import dao.versao_dao

def montar_arquivo_estrutura_conf(versao, banco):
    
    versao = dao.versao_dao.buscar_versao(versao)
    if not versao:
        return resposta('erro', 'Versão '+versao+' não encontrada!')

    script_list = buscar_scripts(versao.versao_id, banco, 'Estrutura Configuracao')

    if script_list:
        json = ''
        for script in script_list:
            json += script.codigo + '\r\n'
        return resposta('estruturas_conf', json)
    else:
        return resposta('erro', 'Registros da '+versao+' não encontrados!')

def resposta(chave, valor):
    return jsonify({chave: valor})