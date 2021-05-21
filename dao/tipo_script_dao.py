import psycopg2
from db import conn

from models.tipo_script import Tipo_Script

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def buscar_tipo_script_by_id(tipo_script_id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT TIPOSCRIPTOID, ORDEM, DESCRICAO "+
                      "from TIPOSCRIPT "+
                     "where TIPOSCRIPTOID = %s::bigint ", (tipo_script_id,))
        tipo_script_data = cur.fetchone()
        cur.close()

        if tipo_script_data:
            return montar_tipo_script(tipo_script_data)
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)

    return None

def buscar_tipo_script_by_desc(descricao):
    try:
        cur = conn.cursor()
        cur.execute("SELECT TIPOSCRIPTOID, ORDEM, DESCRICAO "+
                      "from TIPOSCRIPT "+
                     "where DESCRICAO = %s ", (descricao,))
        tipo_script_data = cur.fetchone()
        cur.close()

        if tipo_script_data:
            return montar_tipo_script(tipo_script_data)
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)

    return None

def montar_tipo_script(tipo_script_data):
    tipo_script = Tipo_Script()
    tipo_script.tipo_script_id = tipo_script_data[0]
    tipo_script.ordem = tipo_script_data[1]
    tipo_script.descricao = tipo_script_data[2]
    return tipo_script