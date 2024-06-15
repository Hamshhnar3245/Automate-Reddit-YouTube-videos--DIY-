import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from Google import Create_Service



CLIENT_SECRET_FILE = '' # SELF EXPLAINING
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']



service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
folder_id = '' # folder id in Google Drive
file_names = ['concatenation.mp4']
mime_types = ['video/mp4']
for file_name, mime_type in zip(file_names, mime_types) :
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
media = MediaFileUpload('./concatenated_video/{0}'.format(file_name), mimetype=mime_type)
service.files().create(
    body=file_metadata,
    media_body = media,
    fields='id'
).execute()


media = None

print("The concatenated video has been uploaded to Google Drive.")


import googledrive_to_deleteCurrentMedia