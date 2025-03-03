import logging
import os
import asyncio
from fastapi import FastAPI
from telegram import Update
from telegram.ext import Application, CommandHandler
import uvicorn

# টেলিগ্রাম বট টোকেন, Render environment variable থেকে সরাসরি নেব
TOKEN = os.getenv("BOT_TOKEN")

# লগ সেটআপ
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI অ্যাপ তৈরি
app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 Welcome to My Telegram Bot API!"}

@app.get("/about")
def about():
    return {"message": "ℹ️ আমি Render-এ হোস্ট করা একটি টেলিগ্রাম বট।"}

# Start Command Handler (Telegram Bot)
async def start(update: Update, context):
    await update.message.reply_text("👋 হ্যালো! আমি তোমার টেলিগ্রাম বট।")

# About Command Handler (Telegram Bot)
async def about(update: Update, context):
    await update.message.reply_text("ℹ️ আমি Render-এ হোস্ট করা একটি টেলিগ্রাম বট।")

# টেলিগ্রাম বট অ্যাপ তৈরি
async def start_telegram_bot():
    # অ্যাপ্লিকেশন তৈরি করুন
    app_bot = Application.builder().token(TOKEN).build()

    # হ্যান্ডলার যোগ করুন
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("about", about))

    # বট চালু করুন
    print("🚀 Telegram Bot is running...")
    await app_bot.run_polling()

# FastAPI সার্ভার চালু করার জন্য
def start_fastapi_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # FastAPI সার্ভার এবং Telegram বটকে একই সাথে চালানো
    loop.create_task(start_telegram_bot())  # টেলিগ্রাম বট
    loop.create_task(start_fastapi_server())  # FastAPI সার্ভার

    loop.run_forever()  # ইভেন্ট লুপ চালু রাখুন
