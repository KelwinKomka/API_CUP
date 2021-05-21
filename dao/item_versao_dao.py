import psycopg2
from db import conn

from models.item_versao import Item_Versao

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def inserir_item_versao(item_versao):
    try:
        cur = conn.cursor()
        cur.execute("insert into ITENSVERSAO (VERSAOOID, DEVOID, TICKETOID, PROJECTOID, MODULO, "+
                                             "APLICACAO, RELEASE, DESCRICAO, TESTE, DATA) "+
                                     "values (%s::bigint, %s::bigint, %s, %s, %s, "+
                                             "%s, %s::bigint, %s, %s, %s)", 
            (item_versao.versao_id, item_versao.dev_id, item_versao.ticket, item_versao.projeto, item_versao.modulo, 
                item_versao.aplicacao, item_versao.release, item_versao.descricao, item_versao.teste, item_versao.data))
        cur.close()
        conn.commit()
        return "Ok"
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        return str(error)

def buscar_itens_versao_by_versao_id(versao_id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT i.VERSAOOID, i.DEVOID, d.NOME, i.TICKETOID, i.PROJECTOID, i.MODULO, i.APLICACAO, "+
                           "i.RELEASE, i.DESCRICAO, i.TESTE, i.DATA"+
                      "from ITENSVERSAO i inner join DEV d on i.DEVOID = d.DEVOID "+
                     "where i.VERSAOOID = %s::bigint", (versao_id,))
        itens_versao_data = cur.fetchall()
        cur.close()

        itens_versao = []

        for item_versao_data in itens_versao_data:
            item_versao = montar_item_versao(item_versao_data)
            itens_versao.append(item_versao)

        return itens_versao
        
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)

    return None

def montar_item_versao(item_versao_data):
    item_versao = Item_Versao()
    item_versao.versao_id = item_versao_data[0]
    item_versao.dev_id = item_versao_data[1]
    item_versao.dev = item_versao_data[2]
    item_versao.ticket = item_versao_data[3]
    item_versao.projeto = item_versao_data[4]
    item_versao.modulo = item_versao_data[5]
    item_versao.aplicacao = item_versao_data[6]
    item_versao.release = item_versao_data[7]
    item_versao.descricao = item_versao_data[8]
    item_versao.teste = item_versao_data[9]
    item_versao.data = item_versao_data[10]
    return item_versao