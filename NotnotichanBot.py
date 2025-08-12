from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random_quotes_generator
from handlers.gmail_handler import get_gmail_service, fetch_unread_emails, mark_as_read
from handlers.outlook_handler import fetch_unread_emails_outlook
import asyncio
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r".\notichan\.env")

token = os.getenv("NOTNOTICHAN_TOKEN")
id = os.getenv("NOTNOTICHAN_ID")

app = ApplicationBuilder().token(token).build()



def notichan_gmail_text():
    service = get_gmail_service()
    emails = fetch_unread_emails(service)
    text = f"{emails}"
    return text

def notichan_outlook_text():
    emails = fetch_unread_emails_outlook()
    text = f"{emails}"
    return text

async def notichan_gmail_text_sender():
    quote = random_quotes_generator.get_random_quotes()
    await app.bot.send_message(chat_id = id, text = f"gm, {quote},\n {notichan_gmail_text()}" )
    await app.bot.send_message(chat_id = id, text = f"{notichan_outlook_text()}")

asyncio.run(notichan_gmail_text_sender())