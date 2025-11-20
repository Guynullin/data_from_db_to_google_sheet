import logging

from pathlib import Path
from db_utils import connect_to_db
from sheets_api import connect_to_table
from config import LOG_PATH, PKL_PATH, XLSX_DICT, SERVICE_FILE, SHOW, SILENT
from tg_bot import send_message, send_message_to_channel

def main() -> None:
    '''
    Collects data from the database and makes changes to the google sheet table.

    :return: None.
    '''
    Path(LOG_PATH).mkdir(parents=True, exist_ok=True)
    Path(PKL_PATH).mkdir(parents=True, exist_ok=True)
    Path(XLSX_DICT['in']).mkdir(parents=True, exist_ok=True)
    Path(XLSX_DICT['out']).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, filename=f"{LOG_PATH}/log.txt", filemode='a',\
                        format="%(asctime)s %(levelname)s %(message)s")

    logging.info(f"Start, show: {SHOW}")
    try:
        status = connect_to_db(show_on_site=SHOW)
        if status != 0:
            logging.error(f"status: {status}, error when connecting to db")
            raise Exception(f"status: {status}, error when connecting to db")
        status = connect_to_table(show_on_site=SHOW, pkl_path=PKL_PATH,\
                        xlsx_dict=XLSX_DICT, service_file=SERVICE_FILE)
        if status == 0:
            logging.info('Success!')
            send_message(f"<client_to_google_sheet> Success")
            if not SILENT:
                send_message_to_channel(f"Таблица 'Для заливки дисков' обновлена успешно")
        else:
            logging.error(f"status: {status}, error when connecting to cloud")
            raise Exception('Возникла ошибка, таблица "Для заливки дисков" не обновлена')
        logging.info('<main> End\n\n')

    except Exception as ex:
        logging.error(f"<main> {ex}\n\n")
        send_message(message=f"Error: {ex}")
        if not SILENT:
            send_message_to_channel(message=f'{ex}')


if __name__ == '__main__':
    main()

