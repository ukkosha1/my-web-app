import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Logging sozlamalari
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Web App URL ni shu yerga qo‘ying (keyinchalik sozlanadi)
WEB_APP_URL = 'https://google.com/'

# /start komandasi uchun handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        "Salom! Men sizga yordam beradigan botman.\n"
        "Quyidagi tugmani bosib, ishni boshlang."
    )

    # Start tugmasi
    keyboard = [
        [KeyboardButton("Start", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Yordam uchun tugma handleri
async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Bu qism Web App orqali boshqariladi
    pass  # Web App tugmasi orqali boshqariladi

# Web App data handleri
async def receive_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=f"TRC20 Manzilingiz: {data}")
    # Foydalanuvchiga xabar yuborish

# Notog‘ri komandalar uchun handler
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kechirasiz, men bunday komandani tushunmayman.")

def main():
    # Bot tokenini shu yerga qo‘ying
    TELEGRAM_BOT_TOKEN = '7229132781:AAGyUp37qQgcaETbIfx098c_ZJ83TZFgrDs'

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Handlerlarni qo‘shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), help_handler))
    application.add_handler(MessageHandler(filters.ALL & filters.StatusUpdate.WEB_APP_DATA, receive_data))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == '__main__':
    main()
