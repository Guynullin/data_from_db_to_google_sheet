import gspread
import logging

def format_style(service_file_path: str, xlsx_dict: dict, sheetName: str):
    '''
    Connects to the Google sheet table and changes the formatting style.
    
    :param sheetName: the name of the table sheet.
    :param xlsx_dict: a dictionary with xlsx data from the configuration file.
    :param service_file_path: a path to google service file.
    :return: zero if success or 1 if error occured.
    '''
    try:
        file_id = xlsx_dict['file_id']
        
        client = gspread.service_account(filename=service_file_path)
        spreadsheet = client.open_by_key(file_id)
        
        sheetName = spreadsheet.worksheet(sheetName)

        current_rows = sheetName.col_values(2)
        number_of_rows = len(current_rows)

        checkbox_request = {
            'requests': [
                {
                    'repeatCell': {
                        'cell': {'dataValidation': {'condition': {'type': 'BOOLEAN'}}},
                        'range': {
                            'sheetId': sheetName.id,
                            'startRowIndex': 1,
                            'endRowIndex': number_of_rows,
                            'startColumnIndex': 9, 'endColumnIndex': 13
                            },
                        'fields': 'dataValidation'
                    }
                }
                ]
            }
        spreadsheet.batch_update(checkbox_request)

        # clear format 
        clean_format = {
            "requests": [
                {
                    "updateCells": {
                        "range": {
                            "sheetId": sheetName.id,
                            "startRowIndex": 1,
                            "endRowIndex": number_of_rows,
                            "startColumnIndex": 9,
                            "endColumnIndex": 13
                        },
                        "fields": "userEnteredFormat"
                    }
                }
            ]
        }
        spreadsheet.batch_update(clean_format)
        # sheet.update('N1', 'FALSE', raw=False)
        
    # Deprecated
    #     # id
    #     hex_color = '#CCCCCC'
    #     sheet.format("A1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     hex_color = '#F4CCCC'
    #     sheet.format("B1:C1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     hex_color = '#D6E6D0'
    #     sheet.format("D1:E1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # diameter
    #     hex_color = '#C9DAF8'
    #     sheet.format("F1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # color
    #     hex_color = '#E69138'
    #     sheet.format("G1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # link to site
    #     hex_color = '#EAD1DC'
    #     sheet.format("H1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # yandex disk
    #     hex_color = '#D9D2E9'
    #     sheet.format("I1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # in stock
    #     hex_color = '#6AA84F'
    #     sheet.format("J1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # white background
    #     hex_color = '#FFFFFF'
    #     sheet.format("K1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # v stand
    #     hex_color = '#F1C232'
    #     sheet.format("L1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
    #     # on car
    #     hex_color = '#CCCCCC'
    #     sheet.format("M1", {
    #     "backgroundColor": {
    #     "red": matplotlib.colors.to_rgb(hex_color)[0],
    #     "green": matplotlib.colors.to_rgb(hex_color)[1],
    #     "blue": matplotlib.colors.to_rgb(hex_color)[2]
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "textFormat": {
    #     "foregroundColor": {
    #         "red": 0.0,
    #         "green": 0.0,
    #         "blue": 0.0
    #     },
    #     "fontSize": 10,
    #     "bold": True
    #     }
    # })
        

        # editor_users_list = ["client.dox@gmail.com", 
        #         "db-bot-client@client-data-from-db.iam.gserviceaccount.com",
        #         "daewoonexia928@mail.ru"]

        # status_prot = spreadsheet.list_protected_ranges(sheetid=sheet.id)
        # print(f"{status_prot}")

        # if len(status_prot) > 0:
        #     logging.info(f"header is protected: \n{status_prot}")
        # else:
        #     logging.warn(f"header is not protected: \n{status_prot}")
        #     request_protect_header = {
        #         "requests": [
        #             {
        #             "addProtectedRange": {
        #                 "protectedRange": {
        #                 "range": {
        #                     "sheetId": sheet.id,
        #                     "startRowIndex": 0,
        #                     "endRowIndex": 1,
        #                     "startColumnIndex": 0,
        #                     "endColumnIndex": 13,
        #                     },
        #                 "description": "Если менять названия столбцов в шапке - парсер сломается, не меняй названия столбцов, ок?",
        #                 "warningOnly": True,
        #                 #"editors": {
        #                 #        "users": editor_users_list
        #                 #        }
        #                     }
        #                 }
        #             }
        #         ]}
        #     spreadsheet.batch_update(request_protect_header)
        #     status_prot = spreadsheet.list_protected_ranges(sheetid=sheet.id)
        #     logging.info(f"now the header is protected: \n{status_prot}")


        # delete protect
        # delete_protect_header = {
        #             "requests": [
        #             {
        #             "deleteProtectedRange": {
        #                 "protectedRangeId": 116655136,
        #                 }
        #             }
        #             ]
        #         }
        # spreadsheet.batch_update(delete_protect_header)
        
        
        # site_link_column_width = {
        #         "requests": [
        #             {
        #                 "updateDimensionProperties": {
        #                     "range": {
        #                         "sheetId": sheet.id,
        #                         "dimension": "COLUMNS",
        #                         "startIndex": 7,
        #                         "endIndex": 8
        #                     },
        #                     "properties": {
        #                         "pixelSize": 450
        #                     },
        #                     "fields": "pixelSize"
        #                 }
        #             }
        #         ]
        #     }
        # spreadsheet.batch_update(site_link_column_width)



        return 0
    
    except Exception as e:
        logging.error(f"<format_style> {e}")
        print(f"<format_style> {e}")
        return 1
    

