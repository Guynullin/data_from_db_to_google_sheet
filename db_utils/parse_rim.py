import logging

# app_product.pic - главное фото
# app_productimage real=false and bottom=false - боковой слайдер
# app_productimage real=true and bottom=false - малый нижний слайдер (v-стойка шоурум)
# app_productimage real=false and bottom=true - большой нижний слайдер (на авто)

# in app_product.data
# replace_pics - замена главного фото
# replace_bottom_pics - замена малого нижнего слайдера  (v-стойка шоурум)
# replace_bottom_slides - замена большого нижнего слайдера (на авто)

def parse_rim(products: list, rim_rows: list, image_rows: list, brands: list):
    """returns a list of the rims cards by their type.

    :param brands: a list of wheel brands from the database.
    :param products: a list with data from the app_products table.
    :param rim_rows: a list with data from the app_rim table.
    :param image_rows: a list of product images from the app_productimage table.
    :return: a list of the rims cards or 1 when error occured.
    """
    logging.info(f'start parsing the cards, len rim_rows: {len(rim_rows)}')
    cards = []
    count = 0
    for rim in rim_rows:
        
        count += 1

        card = {'id': rim[0]}
        if rim[1] != None:
            card['diameter'] = rim[1]
        else:
            card['diameter'] = ''
        if rim[4] != None:
            card['bolts'] = rim[4]
        else:
            card['bolts'] = ''
        if rim[5] != 0:
            card['bolts2'] = rim[5]
        if rim[7] != None:
            card['pcd'] = rim[7]
        else:
            card['pcd'] = ''
        if rim[8] != 0:
            card['pcd2'] = rim[8]
        card['width'] = rim[3]
        card['et'] = rim[2]
        card['dia'] = rim[6]
        card['color'] = rim[14]
        card['type'] = rim[11]
        card['et2'] = rim[12]
        card['width2'] = rim[13]

        for prod in products:
            if prod[0] == rim[0]:
                card['title'] = prod[2].replace('В СТИЛЕ', 'в стиле').replace('В стиле', 'в стиле')
                if prod[3] != None:
                    card['slug'] = prod[3]
                else:
                    break
                if prod[21] != None and prod[6] != None and prod[21] > prod[6]:
                    card['price'] = int(prod[21])
                elif prod[21] != None:
                    card['price'] = int(prod[21])
                elif prod[6] != None:
                    card['price'] = int(prod[6])
                else:
                    card['price'] = None

                card['brand_id'] = prod[9]
                if card['brand_id'] != None and isinstance(card['brand_id'], int):
                    for brand_row in brands:
                        if brand_row[0] == card['brand_id']:
                            card['brand'] = brand_row[1]
                            break

                card['model'] = prod[10]
                
                # главное фото
                card['pic'] = prod[5]
                show = prod[14]
                card['show'] = True if show else False

                data = prod[16]
                if isinstance(data, dict):
                    # замена главного фото
                    if 'replace_pics' in data and data['replace_pics'] != None:
                        if isinstance(data['replace_pics'], list)\
                        and len(data['replace_pics']) > 0:
                            card['replace_pics'] = data['replace_pics']
                        elif isinstance(data['replace_pics'], str):
                            card['replace_pics'] = [data['replace_pics']]
                    # замена малого нижнего слайдера  (v-стойка шоурум) 
                    if 'replace_bottom_pics' in data and data['replace_bottom_pics'] != None:
                        if isinstance(data['replace_bottom_pics'], list)\
                        and len(data['replace_bottom_pics']) > 0:
                            card['replace_bottom_pics'] = data['replace_bottom_pics']
                        elif isinstance(data['replace_bottom_pics'], str):
                            card['replace_bottom_pics'] = [data['replace_bottom_pics']]
                    # замена большого нижнего слайдера (на авто)
                    if 'replace_bottom_slides' in data and data['replace_bottom_slides'] != None:
                        if isinstance(data['replace_bottom_slides'], list)\
                        and len(data['replace_bottom_slides']) > 0:
                            card['replace_bottom_slides'] = data['replace_bottom_slides']
                        elif isinstance(data['replace_bottom_slides'], str):
                            card['replace_bottom_slides'] = [data['replace_bottom_slides']]
        
        if 'slug' not in card:
            continue

        image_row_list = []
        for image_row in image_rows:
            if image_row[2] == card['id']:
                image_row_list.append(image_row)
        
        additional_pics = []
        bottom_pics = []
        bottom_slides = []

        for image_row in image_row_list:
            if image_row[3] == False and image_row[4] == False:
                additional_pics.append(image_row[1])
            elif image_row[3] == True and image_row[4] == False:
                bottom_pics.append(image_row[1])
            elif image_row[3] == False and image_row[4] == True:
                bottom_slides.append(image_row[1])
        if len(additional_pics) > 0:
            card['additional_pics'] = additional_pics
        if len(bottom_pics) > 0:
            card['bottom_pics'] = bottom_pics
        if len(bottom_slides) > 0:
            card['bottom_slides'] = bottom_slides

        if 'bottom_pics' in card or 'replace_bottom_pics' in card:
            card['v_stand'] = True
        else:
            card['v_stand'] = False
        
        if 'bottom_slides' in card or 'replace_bottom_slides' in card:
            card['on_car'] = True
        else:
            card['on_car'] = False

        if 'bolts2' in card:
            card['bolts'] = f"{card['bolts'] + card['bolts2']}"
        if 'pcd2' in card:
            card['pcd'] = f"{card['pcd']}/{card['pcd2']}"
        

        cards.append(card)

    if len(cards) > 0:
        return cards
    else:
        return 1