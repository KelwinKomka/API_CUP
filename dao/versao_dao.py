import psycopg2
from db import conn

from models.versao import Versao

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def inserir_versao(versao):
    try:
        cur = conn.cursor()
        cur.execute("insert into VERSAO (MAJOR, MINOR, BANCO, DATA, DESENVOLVIMENTO, "+
                                        "PRODUCAO, HABILITADA) "+
                                "values (%s::bigint, %s::bigint, %s::bigint, %s, %s, "+
                                        "%s, %s)", 
            (versao.major, versao.minor, versao.banco, versao.data, versao.dev, versao.prod, versao.habilitada))
        cur.close()
        conn.commit()
        return "Ok"
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        return str(error)

def buscar_versao(versao):
    try:
        valores_versao = versao.split('.')
        major = valores_versao[0]
        minor = valores_versao[1]
        banco = valores_versao[2]
    except (Exception,) as error:
        return None

    try:
        cur = conn.cursor()
        cur.execute("SELECT VERSAOOID, MAJOR, MINOR, BANCO, DATA, DESENVOLVIMENTO, PRODUCAO, HABILITADA "+
                      "from VERSAO v "+
                     "where v.MAJOR = %s::bigint "+
                       "and v.MINOR = %s::bigint "+
                       "and v.BANCO = %s::bigint", (major, minor, banco))
        versao_data = cur.fetchone()
        cur.close()

        if versao_data:
            return montar_versao(versao_data)     
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)

    return None

def montar_versao(versao_data):
    versao = Versao()
    versao.versao_id = versao_data[0]
    versao.major = versao_data[1]
    versao.minor = versao_data[2]
    versao.banco = versao_data[3]
    versao.data = versao_data[4]
    versao.dev = versao_data[5]
    versao.prod = versao_data[6]
    versao.habilitada = versao_data[7]
    return versao