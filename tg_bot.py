import time
import logging
import requests

from config import BOT_TOKEN, CHAT_ID, CHAN_CHAT_ID, CHAN_TOKEN, TG_HEADER

def send_message(message:str) -> None:
    """Send message to telegram dispatcher.

    :param message: a string with the message.
    :return: None.
    """
    err = 0
    message = f"{TG_HEADER}\n{message}".replace(BOT_TOKEN, '<token>')\
        .replace(CHAT_ID, '<chat_id>')
    while True:
        try:
            if err >= 15:
                logging.error('Stopping the send_message function. Exceeded the number of connection attempts')
                break
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
            requests.get(url, timeout=60)
            break
        except requests.exceptions.ConnectionError as connecterr:
            err += 1
            logging.error(connecterr)
            time.sleep(15)

        except Exception as ex:
            err += 1
            logging.error(ex)
            time.sleep(15)
        

def send_message_to_channel(message:str) -> None:
    """Send message to telegram dispatcher channel.

    :param message: a string with the message.
    :return: None.
    """
    message = f"{TG_HEADER}\n{message}".replace(CHAN_TOKEN, '<token>').replace(CHAN_CHAT_ID, '<chat_id>')
    err_count = 0
    while True:
        if err_count >= 15:
            logging.error("<send_message_to_channel> errors >= 15, stop")
            break
        try:
            url = f"https://api.telegram.org/bot{CHAN_TOKEN}/sendMessage?chat_id={CHAN_CHAT_ID}&text={message}"
            requests.get(url, timeout=60)
            break
        except requests.exceptions.ConnectionError as connecterr:
            err_count += 1
            logging.error(f"<send_message_to_channel> {connecterr}")
            time.sleep(15)
        except Exception as ex:
            err_count += 1
            logging.error(f"<send_message_to_channel> {ex}")
            time.sleep(15)
