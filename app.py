import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading

# Flask অ্যাপ ইনিশিয়ালাইজ করুন
app = Flask(__name__)

# টেলিগ্রাম বট টোকেন (Render.com এ environment variable হিসেবে সেট করুন)
TOKEN = os.environ.get('BOT_TOKEN')

# Flask রুটস
@app.route('/')
def home():
    return "বট সচল রয়েছে! ✅"

@app.route('/about')
def about():
    return "আমার সম্পর্কে তথ্য: আমি একজন ডেভেলপার, টেলিগ্রাম বট বানাতে পছন্দ করি।"

# টেলিগ্রাম বট হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো! আমি আপনার বট। /about লিখে আমার সম্পর্কে জানুন।")

def run_bot():
    """টেলিগ্রাম বট রান করুন"""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    # বটকে আলাদা থ্রেডে রান করুন
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    
    # Flask অ্যাপ রান করুন
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
