import logging


def process_xlsx(cards: list, xlsx_dict: dict, ws):
    ''' 
    Makes changes to excel file and save it to the path from xlsx_dict.

    :param cards: product cards from the pkl file.
    :param xlsx_dict: a dictionary with xlsx data from the configuration file.
    :param ws: a openpyxl worksheet object.
    :return: zero if success or 1 if error occured.
    '''
    ok_cards = []

    try:
        if not (ws[1][0].value == 'id'):
            raise Exception(f'|id| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][1].value == 'ПРОИЗВОДИТЕЛЬ'):
            raise Exception(f'|ПРОИЗВОДИТЕЛЬ| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][2].value == 'МОДЕЛЬ'):
            raise Exception(f'|МОДЕЛЬ| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][3].value == 'КОЛ-ВО ОТВЕРСТИЙ'):
            raise Exception(f'|КОЛ-ВО ОТВЕРСТИЙ| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][4].value == 'РАЗБОЛТОВКА'):
            raise Exception(f'|РАЗБОЛТОВКА| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][5].value == 'ДИАМЕТР'):
            raise Exception(f'|ДИАМЕТР| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][6].value == 'ЦВЕТ'):
            raise Exception(f'|ЦВЕТ| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][7].value == 'ССЫЛКА НА САЙТ'):
            raise Exception(f'|ССЫЛКА НА САЙТ| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][9].value == 'НАЛИЧИЕ'):
            raise Exception(f'|НАЛИЧИЕ| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][10].value == 'БЕЛЫЙ ФОН'):
            raise Exception(f'|БЕЛЫЙ ФОН| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][11].value == 'V-СТОЙКА'):
            raise Exception(f'|V-СТОЙКА| wrong title in {xlsx_dict["filename"]}')
        if not (ws[1][12].value == 'АВТО'):
            raise Exception(f'|АВТО| wrong title in {xlsx_dict["filename"]}')
        logging.info(f'<process_xlsx> The number of rows from db: {len(cards)}')

        for index, row in enumerate(ws.rows):
            if index == 0:
                continue
            for card in cards:
                if card['id'] == row[0].value:
                    row[1].value = card['brand'] if 'brand' in card else ''
                    row[2].value = card['model'] if 'model' in card else ''
                    row[3].value = card['bolts'] if 'bolts' in card else ''
                    row[4].value = card['pcd'] if 'pcd' in card else ''
                    row[5].value = card['diameter'] if 'diameter' in card else ''
                    row[6].value = card['color'] if 'color' in card else ''
                    row[7].value = "https://client.ru/diski/" + card['slug']
                    row[7].style = 'Hyperlink'
                    row[9].value = card['show'] if 'show' in card else False
                    if row[10].value == '=FALSE()':
                        row[10].value = False
                    elif row[10].value == '=TRUE()':
                        row[10].value = True
                    row[11].value = card['v_stand'] if 'v_stand' in card else False
                    row[12].value = card['on_car'] if 'on_car' in card else False
                    ok_cards.append(card)
                    break
        
        new_cards = [x for x in cards if x not in ok_cards] 
        max_row = ws.max_row + 1
        for index, card in enumerate(new_cards):
            ws[max_row + index][0].value = card['id']
            ws[max_row + index][1].value = card['brand'] if 'brand' in card else ''
            ws[max_row + index][2].value = card['model'] if 'model' in card else ''
            ws[max_row + index][3].value = card['bolts'] if 'bolts' in card else ''
            ws[max_row + index][4].value = card['pcd'] if 'pcd' in card else ''
            ws[max_row + index][5].value = card['diameter'] if 'diameter' in card else ''
            ws[max_row + index][6].value = card['color'] if 'color' in card else ''
            ws[max_row + index][7].value = "https://client.ru/diski/" + card['slug']
            ws[max_row + index][7].style = 'Hyperlink'
            ws[max_row + index][9].value = card['show'] if 'show' in card else False
            ws[max_row + index][10].value = False
            ws[max_row + index][11].value = card['v_stand'] if 'v_stand' in card else False
            ws[max_row + index][12].value = card['on_car'] if 'on_car' in card else False

        logging.info(f"cards from db: {len(cards)}")
        logging.info(f"matching cards from xlsx: {len(ok_cards)}")
        logging.info(f"new cards: {len(new_cards)}")

        return 0

    except Exception as e:
        logging.error(f'<process_xlsx> {e}')
        return 1
    


