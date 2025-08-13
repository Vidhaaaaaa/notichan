from imap_tools import MailBox, AND
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r".\notichan\.env")

# fetching server, user, password from .env
server = os.getenv("IMAP_ADDRESS")
user = os.getenv("OUTLOOK_USER")
password = os.getenv("USER_PASSWORD")

messages = []

# function to fetch unread emails from outlook as a list of dictionaries
def fetch_unread_emails_outlook():

    # opening mailbox with 'with' so that it closes itself even if there are any other errors
    with MailBox(server).login(user, password) as mailbox:
        emails = list(mailbox.fetch(criteria=AND(seen=False), mark_seen=True, bulk=True, reverse=True))[:5] # bulk= True means it'll fetch all the unread emails at once, [:5] means only last 5

        for e in emails:
            id  = e.uid
            date = e.date_str
            from_ = e.from_ # so that from_ does not mix up with the keyword 'from'
            subject = e.subject
            text = e.text[:100] # it'll give a snippet kind of, with first 100 characters
        
            messages.append({
                "id": id,
                "date": date,
                "from": from_,
                "subject": subject,
                "snippet": text
            })

    return messages