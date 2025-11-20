import logging
import pickle

from config import PKL_PATH
from pathlib import Path
from .parse_rim import parse_rim



def get_data_from_db(conn, online: bool):
    '''
    Requests data from the database and creates a list with product cards 
        and writes them to a pkl file.

    :param conn: a connection object.
    :param online: a bool status of product cards.
    :return: zero if success.
    '''
    with conn.cursor() as curs:

        logging.info(f'requesting data from tables, online: {online}')
        # rim pages published on the website
        # get rims alloy + forged from app_product 
        if online:
            curs.execute("SELECT * FROM app_product WHERE LOWER(name) LIKE LOWER('%диск%') AND show=true")
        else:
            curs.execute("SELECT * FROM app_product WHERE LOWER(name) LIKE LOWER('%диск%') AND show=false")

        products = curs.fetchall()
        rims_id_list = []
        for prod in products:
            id = prod[0]
            rims_id_list.append(id)

        # get all brands from app_brand
        curs.execute(f"SELECT * FROM app_brand")
        brands = curs.fetchall()

        # get rims from app_rim by id
        rims_id_list = list(map(str, rims_id_list))
        curs.execute(f"SELECT * FROM app_rim WHERE product_ptr_id IN ({','.join(rims_id_list)})")
        rim_rows = curs.fetchall()
        
        # get rims from app_productimage by id
        curs.execute(f"SELECT * FROM app_productimage WHERE product_id IN ({','.join(rims_id_list)})")
        image_rows = curs.fetchall()
        
        # parse cards
        cards_online = parse_rim(products=products, rim_rows=rim_rows, image_rows=image_rows, brands=brands)
        
        pkl_filename = 'file.pkl'
        if online:
            pkl_filename = 'online.pkl'
        else:
            pkl_filename = 'offline.pkl'

        if cards_online != 1 and isinstance(cards_online, list) and len(cards_online) > 0:
            logging.info(f"number of cards: {len(cards_online)}")
            Path(PKL_PATH).mkdir(parents=True, exist_ok=True)
            with open(f"{PKL_PATH}/{pkl_filename}", 'wb') as file:
                pickle.dump(cards_online, file=file)
                logging.info(f"{len(cards_online)} cards is recorded in {pkl_filename}")
            logging.info(f'Success! {pkl_filename} is recorded')
        else:
            logging.error(f"cards_online is empty")
            return 1
    return 0