import os
import logging

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

def get_service(api_name, api_version, scopes, key_file_location):
    """
    Get a service that communicates to a Google API.

    :param api_name: the name of the api to connect to.
    :param api_version: the api version to connect to.
    :param scopes: a list auth scopes to authorize for the application.
    :param key_file_location: the path to a valid service account JSON key file.

    :return: a service that is connected to the specified API.
    """

    credentials = service_account.Credentials.from_service_account_file(
    key_file_location)

    scoped_credentials = credentials.with_scopes(scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=scoped_credentials)

    return service


def upload_xlsx(xlsx_dict: dict, service_file_path: str):
  '''
  Connects to the google sheet table and uploads xlsx file.

  :param xlsx_dict: a dictionary with xlsx data from the configuration file.
  :param service_file: a path to google service file.
  :return: zero if success or 1 if error occured.
  '''
  scopes =  [
    'https://www.googleapis.com/auth/drive'
    ]
  file_path = os.path.join(xlsx_dict['out'], f"{xlsx_dict['filename']}.xlsx")
  file_id = xlsx_dict['file_id']
  try:
    service = get_service(api_name='drive', api_version='v3', scopes=scopes, key_file_location=service_file_path)
    file_metadata = {
        "name": os.path.splitext(os.path.basename(file_path))[0],
        "mimeType": "application/vnd.google-apps.spreadsheet",
    }
    media = MediaFileUpload(filename=file_path,\
                            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",\
                            resumable=True)

    response = (
        service.files()
        .update(body=file_metadata, media_body=media, fileId=file_id)
        .execute()
    )

    logging.info(f"File with id={file_id} has been uploaded.")
    return 0

  except HttpError as error:
    logging.error(f"<upload_xlsx> HttpError: {error}")
    return 1

  except Exception as e:
    logging.error(f"<upload_xlsx> {error}")
    return 1



