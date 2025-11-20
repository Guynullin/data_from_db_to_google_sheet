import psycopg2
import logging
from sshtunnel import SSHTunnelForwarder

from .get_data_from_db import get_data_from_db
from config import SSH_HOST, SSH_USERNAME, SSH_PASSWORD, LOCAL_HOST, LOCAL_PORT,\
    REMOTE_PORT, DB_NAME, DB_USER, DB_PASSWORD


def connect_to_db(show_on_site: dict):
    '''
    Connect to database and collect product cards.

    :param show_on_site: a dictionary with the collection statuses of product cards.
    :return: zero if success.
    '''

    try:
        with SSHTunnelForwarder(
            ssh_address_or_host = SSH_HOST,  
            ssh_username = SSH_USERNAME,
            ssh_password = SSH_PASSWORD,
            local_bind_address  = (LOCAL_HOST, LOCAL_PORT),
            remote_bind_address = (LOCAL_HOST, REMOTE_PORT)
        ) as server:
            logging.info('\n\n<connect_to_db> starting to connect to the database')
            server.start()

            params = {
                'database': DB_NAME,
                'user': DB_USER,
                'password': DB_PASSWORD,
                'host': LOCAL_HOST,
                'port': LOCAL_PORT
                }

            conn = psycopg2.connect(**params)
            status1 = 0
            status2 = 0
            if show_on_site['online'] and show_on_site['offline']:
                status1 = get_data_from_db(conn=conn, online=True)
                status2 = get_data_from_db(conn=conn, online=False)
            elif show_on_site['online']:
                status1 = get_data_from_db(conn=conn, online=True)
            elif show_on_site['offline']:
                status2 = get_data_from_db(conn=conn, online=False)

            logging.info('<connect_to_db> closing the connection')

            if status1 != 0:
                return status1
            elif status2 != 0:
                return status2
            else:
                return 0
        

    except Exception as ex:
        logging.error(f"{ex}\n\n")
        return 1



