import psycopg2
from db import conn

from models.dev import Dev

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def buscar_dev(login):
    try:
        cur = conn.cursor()
        cur.execute("SELECT DEVOID, NOME, ID, SENHA, HABILITADO "+
                      "from DEV "+
                     "where ID = %s", (login,))
        dev_data = cur.fetchone()
        cur.close()

        if dev_data:
            return montar_dev(dev_data)     
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)

    return None

def montar_dev(dev_data):
    dev = Dev()
    dev.dev_id = dev_data[0]
    dev.nome = dev_data[1]
    dev.id = dev_data[2]
    dev.senha = dev_data[3]
    dev.habilitado = dev_data[4]
    return dev