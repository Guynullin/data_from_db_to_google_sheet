import logging
import gspread
import os

from gspread.utils import ExportFormat

def download_xlsx(service_file_path: str, xlsx_dict: dict):
    '''
    Connects to the google sheet table and downloads it in excel format.

    :param xlsx_dict: a dictionary with xlsx data from the configuration file.
    :param service_file: a path to google service file.
    :return: zero if success or 1 if error occured.
    '''
    try:

        gc = gspread.service_account(filename=service_file_path)
        
        sh = gc.open(xlsx_dict['filename'])
        
        export_file = sh.export(format=ExportFormat.EXCEL)
        
        save_path = os.path.join(xlsx_dict['in'], f"{xlsx_dict['filename']}.xlsx")
        with open(save_path, 'wb') as file:
            file.write(export_file)
        
        logging.info(f"<download_xlsx> {xlsx_dict['filename']}.xlsx is saved successful")
        
        return 0
    
    except Exception as ex:

        logging.error(f"<download_xlsx> {ex}")

        return 1
    
