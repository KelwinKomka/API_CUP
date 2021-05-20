import psycopg2
from db import conn

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def inserir_script(chat_id, user_id, name):
    try:
        cur = conn.cursor()
        cur.execute("insert into SCRIPT (CHATID, USUARIOID, NOME) values (%s::bigint, %s::bigint, %s)", (chat_id, user_id, name))
        cur.close()
        conn.commit()
        return "Ok"
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        return str(error)