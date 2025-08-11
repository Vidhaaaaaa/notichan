from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r".\notichan\.env")

token = os.getenv("NOTNOTICHAN_TOKEN")
id = os.getenv("NOTNOTICHAN_ID")

app = ApplicationBuilder().token(token).build()

async def notichan_text_sender():
    await app.bot.send_message(chat_id = id, text = "hi")