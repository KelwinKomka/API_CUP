import psycopg2
from db import conn

from models.script import Script

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def inserir_script(script):
    try:
        cur = conn.cursor()
        cur.execute("insert into SCRIPT (VERSAOOID, TIPOSCRIPTOID, DESCRICAO, CODIGO, SKIP, "+
                                        "TIPOBANCO, OLDCODIGO, ORDEM, BANCO) "+
                                "values (%s::bigint, %s::bigint, %s, %s, %s, "+
                                        "%s, %s, %s::bigint, %s)", 
            (script.versao_id, script.tipo_script_id, script.descricao, script.codigo, script.skip, script.tipobanco, script.oldcodigo, script.ordem, script.banco))
        cur.close()
        conn.commit()
        return "Ok"
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        return str(error)

def buscar_scripts(versao_id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT t.DESCRICAO TIPOSCRIPT, s.DESCRICAO, s.CODIGO, s.SKIP, "+
                           "s.TIPOBANCO, s.OLDCODIGO, s.BANCO "+
                      "from SCRIPT s inner join TIPOSCRIPT t on s.TIPOSCRIPTOID = t.TIPOSCRIPTOID "+
                     "where s.VERSAOOID = %s::bigint "+
                     "order by t.ORDEM", (versao_id,))
        scripts_data = cur.fetchall()
        cur.close()

        scripts = []

        for script_data in scripts_data:
            script = montar_script(script_data)
            scripts.append(script)
        return scripts
        
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)

    return None

def montar_script(script_data):
    script = Script()
    script.tipo_script = script_data[0]
    script.descricao = script_data[1]
    script.codigo = bytes(script_data[2])
    script.skip = script_data[3]
    script.tipo_banco = script_data[4]
    script.old_codigo = bytes(script_data[5])
    script.banco = script_data[6]

    return script