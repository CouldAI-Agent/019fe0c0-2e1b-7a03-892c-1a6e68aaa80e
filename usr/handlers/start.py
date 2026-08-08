from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

PASSWORD = "theafexar"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user is already authenticated
    if context.user_data.get("authenticated"):
        await show_main_menu(update, context)
    else:
        await update.message.reply_text("🔒 Please enter the password to access the bot:")

async def password_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ignore if already authenticated
    if context.user_data.get("authenticated"):
        return

    text = update.message.text.strip()
    if text == PASSWORD:
        context.user_data["authenticated"] = True
        await update.message.reply_text("✅ Password correct! Access Granted.")
        await show_main_menu(update, context)
    else:
        await update.message.reply_text("❌ Incorrect Password! Access Denied.")

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💹 Select Pair", callback_data="menu_pair"),
         InlineKeyboardButton("📈 Live Signal", callback_data="menu_signal")],
        [InlineKeyboardButton("📸 Upload Chart (AI Vision)", callback_data="menu_vision")],
        [InlineKeyboardButton("📜 Signal History", callback_data="menu_history"),
         InlineKeyboardButton("📒 Trade Journal", callback_data="menu_journal")],
        [InlineKeyboardButton("📊 Performance Dashboard", callback_data="menu_dashboard")],
        [InlineKeyboardButton("ℹ About", callback_data="menu_about")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = "🚀 *Welcome to the Advanced Trading Bot*\nSelect an option below:"
    
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")