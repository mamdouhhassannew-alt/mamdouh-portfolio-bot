import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

WHATSAPP_LINK = "https://wa.me/201224519695"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📞 تواصل", callback_data='contact')],
        [InlineKeyboardButton("📄 CV", callback_data='cv')],
    ]
    await update.message.reply_text("اهلا بيك 👋", reply_markup=InlineKeyboardMarkup(keyboard))

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'contact':
        await query.edit_message_text(f"واتساب: {WHATSAPP_LINK}")
    else:
        await query.edit_message_text("سيتم اضافة CV هنا")

if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(buttons))
    print("Bot is running... @MamdouhPortfolio_bot")
    application.run_polling()