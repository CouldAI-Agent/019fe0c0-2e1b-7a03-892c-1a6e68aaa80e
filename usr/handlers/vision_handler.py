import os
from telegram import Update
from telegram.ext import ContextTypes
from engine.vision_engine import analyze_chart_image

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("authenticated"):
        return
        
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    
    # Download the photo temporarily
    file_path = f"temp_chart_{update.message.chat_id}.jpg"
    await file.download_to_drive(file_path)
    
    await update.message.reply_text("🔍 Analyzing chart screenshot with AI Vision... Please wait.")
    
    try:
        analysis_result = analyze_chart_image(file_path)
        await update.message.reply_text(f"🤖 *AI Vision Analysis*\n\n{analysis_result}", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error during analysis: {str(e)}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)