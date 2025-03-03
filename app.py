from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

app = Flask(__name__)

# টেলিগ্রাম বটের টোকেন
TOKEN = '7791721807:AAFXMz-wyzDjIeqbTdaUYPTP2_HPjmRnv94'

# Flask রুট
@app.route('/')
def home():
    return "Welcome to my Telegram Bot and About Me Page!"

@app.route('/about')
def about():
    return "This is the About Me page. Here you can write something about yourself."

# টেলিগ্রাম বটের হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your Telegram Bot.')

async def about_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is the About Me section of the bot.')

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("about", about_bot))
    application.run_polling()

if __name__ == '__main__':
    # টেলিগ্রাম বট এবং Flask সার্ভার একসাথে চালু করুন
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=5000)
