from telegram import Update
from telegram.ext import ContextTypes
from handlers.start import show_main_menu
from engine.ai_engine import generate_live_signal
from utils.dashboard import get_performance_stats

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "menu_main":
        await show_main_menu(update, context)
    
    elif data == "menu_pair":
        await query.message.edit_text(
            "💹 *Select Pair*\nCurrently analyzing major pairs automatically. More pairs coming soon.\n\nUse 'Live Signal' to analyze EURUSD.",
            parse_mode="Markdown"
        )
        
    elif data == "menu_signal":
        await query.message.edit_text("⏳ Generating live signal. Please wait...")
        signal_result = generate_live_signal("EURUSD")
        await query.message.reply_text(f"📈 *Live Signal Result*\n\n{signal_result}", parse_mode="Markdown")
        
    elif data == "menu_vision":
        await query.message.edit_text("📸 *AI Vision*\nPlease upload a screenshot of your chart. (Send as Photo)")
        
    elif data == "menu_dashboard":
        stats = get_performance_stats(context.user_data)
        await query.message.edit_text(f"📊 *Performance Dashboard*\n\n{stats}", parse_mode="Markdown")
        
    elif data in ["menu_history", "menu_journal", "menu_about"]:
        await query.message.edit_text("Feature under construction. /start to return.")