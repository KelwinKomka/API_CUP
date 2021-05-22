from dao.script_dao import buscar_scripts
from flask import jsonify

import dao.versao_dao

def montar_arquivo_info(versao, banco):
    versao = dao.versao_dao.buscar_versao(versao)
    if not versao:
        return resposta('erro', 'Versão '+versao+' não encontrada!')

    script_list = buscar_scripts(versao.versao_id, banco)

    if script_list:
        json = ''
        for script in script_list:
            json += script.descricao + '.|\r\n'

        return resposta('info', json)
    else:
        return resposta('erro', 'Registros da '+versao+' não encontrados!')

def resposta(chave, valor):
    return jsonify({chave: valor})