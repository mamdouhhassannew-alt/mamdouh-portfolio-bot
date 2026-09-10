import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

from flask import Flask
import threading
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

WHATSAPP_LINK = "https://wa.me/201224519695"
WEBSITE_LINK = "https://mamdouhhassannew-alt.github.io/mamdouh-portfolio-bot/"
WORKS_LINK = "https://mamdouhhassannew-alt.github.io/mamdouh-portfolio-bot/"

# سيرفر مجاني لـ Render
app = Flask('')
@app.route('/')
def home(): return "Mamdouh Bot is Alive - 200 OK"
def run_flask():
    app.run(host='0.0.0.0', port=10000)
threading.Thread(target=run_flask).start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💬 واتساب مباشر", url=WHATSAPP_LINK)],
        [InlineKeyboardButton("🌐 موقعي الرسمي", url=WEBSITE_LINK)],
        [InlineKeyboardButton("📚 أعمالي - صور و PDF", url=WORKS_LINK)]
    ]
    await update.message.reply_text("أهلاً بيك في Mamdouh Book Tools 📚\nاختار من تحت:", reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
