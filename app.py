from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# টোকেন আপনার বটের টোকেন দিয়ে প্রতিস্থাপন করুন
TOKEN = '7791721807:AAFXMz-wyzDjIeqbTdaUYPTP2_HPjmRnv94'

# /start কমান্ডের জন্য হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('হ্যালো! আমি আপনার টেলিগ্রাম বট।')

# /about কমান্ডের জন্য হ্যান্ডলার
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('আমি একটি টেলিগ্রাম বট। আমার সম্পর্কে আরও তথ্য এখানে।')

def main():
    # অ্যাপ্লিকেশন তৈরি করুন
    application = Application.builder().token(TOKEN).build()

    # কমান্ড হ্যান্ডলার যোগ করুন
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("about", about))

    # বট চালু করুন
    application.run_polling()

if __name__ == '__main__':
    main()
