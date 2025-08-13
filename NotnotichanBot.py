from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# import random_quotes_generator
from handlers.gmail_handler import get_gmail_service, fetch_unread_emails, mark_as_read
# from handlers.outlook_handler import fetch_unread_emails_outlook
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("NOTNOTICHAN_TOKEN")
id = os.getenv("NOTNOTICHAN_ID")

app = ApplicationBuilder().token(token).build()



def notichan_gmail_text():
    service = get_gmail_service()
    emails = fetch_unread_emails(service)

    if not emails:
        return "No new emails 😌"

    text_lines = []
    for email in emails:
        sender = email.get("from", "Unknown sender")
        subject = email.get("subject", "No subject")
        date = email.get("date", "No date")
        snippet = email.get("snippet", "")
        text_lines.append(f"📧 {date} \n {sender}: \n{subject}\n\n{snippet} \n - - - \n")
    
        mark_as_read(service, email["id"])

    return "\n\n".join(text_lines)

# def notichan_outlook_text():
#     emails = fetch_unread_emails_outlook()
#     text = f"{emails}"
#     return text

async def notichan_text_sender():
    # quote = random_quotes_generator.get_random_quotes()
    await app.bot.send_message(chat_id = id, text = f"gm,\n {notichan_gmail_text()}" )
    # await app.bot.send_message(chat_id = id, text = f"{notichan_outlook_text()}")
