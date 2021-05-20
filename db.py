import psycopg2

conn = None

def connect_db(config):
    if config.has_section('Database'):
        conn = psycopg2.connect(
            host=config['Database']['host'],
            database=config['Database']['name'],
            user=config['Database']['user'],
            password=config['Database']['password'])
    else:
        raise Exception('Erro ao conectar ao banco de dados!')