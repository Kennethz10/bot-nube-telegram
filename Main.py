import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.environ.get("8007487795:AAE4FNd8vzb7u9tvZqJRxNNCa38T7DE7W-E")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola. Soy tu bot y guardaré lo que me envíes en este chat.")

async def guardar_archivo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    archivo = update.message.document or update.message.video or update.message.audio or update.message.photo
    if archivo:
        await update.message.forward(chat_id=update.message.from_user.id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL | filters.Video.ALL | filters.Audio.ALL | filters.PHOTO, guardar_archivo))

app.run_polling()
