import os
import threading
from flask import Flask
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from handlers.start import start_command, password_handler
from handlers.buttons import button_handler
from handlers.vision_handler import handle_photo

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_TOKEN")

# Flask Keep-Alive Server
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running 24/7!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

def main():
    # Start Flask server in a background thread
    threading.Thread(target=run_flask, daemon=True).start()

    # Initialize Telegram Bot Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Register Handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, password_handler))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Run the bot
    print("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()