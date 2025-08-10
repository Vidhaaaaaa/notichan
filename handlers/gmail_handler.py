from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        
    service = build("gmail", "v1", credentials=creds)
    return service
    
    
user_id =  'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

def fetch_unread_emails(service):
    
    # Getting all the unread messages from Inbox (a dictionary of whole lotta data)
    results = service.users().messages().list(userId= user_id,labelIds=[label_id_one, label_id_two], maxResults=5).execute()
    # labelIds can be changed accordingly

    messages = []

    # unread emails ke ids in a list of dictionaries
    unread_email_ids = results.get("messages", [])

    # this is the content of the messages, taking out one by one
    for msg in unread_email_ids:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data.get('snippet', "") # small snippet of the email
        msg_id = msg_data.get('id', "") # get id of the email

        pl = msg_data["payload"]
        hdr = pl["headers"]

        # extracting the email id the email was sent from
        for i in hdr:
            if i["name"] == "From":
                msg_from = i["value"]

        # extracting the date of email
        for j in hdr:
            if j["name"] == "Date":
                msg_date = j["value"]
        
        #extracting the subject of email
        for k in hdr:
            if k["name"] == "Subject":
                msg_subject = k["value"]


        messages.append({
            "id": msg_id,
            "date": msg_date,
            "from_": msg_from,
            "subject": msg_subject,
            "snippet": snippet,
        })
        
    return messages

def mark_as_read(service, msg_id):
        service.users().messages().modify(
            userId='me',
            id= msg_id,
            body={'removeLabelIds': ['UNREAD']}
        ).execute()
    