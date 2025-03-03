import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is Running!"

@app.route('/about')
def about():
    return "This is a simple Telegram bot running on Render!"

@app.route(f'/{TOKEN}', methods=['POST'])
async def webhook():
    update = Update.de_json(request.get_json(), bot)
    await app.bot.update_queue.put(update)
    return "OK", 200

async def start(update: Update, context):
    await update.message.reply_text("Hello! I am your bot.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    app.bot = application
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
