import os
import json
from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import sys
print("Python version:", sys.version)
print("STEP 1: bot.py loaded")
def main():
    print("STEP 2: main() started")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    print("STEP 3: Application built")
# Load .env locally (Render ignores it and uses Env Vars)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
print("BOT_TOKEN value:", BOT_TOKEN)
WEB_APP_URL = "https://abrahambekele2090.github.io/telegram-webapp/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🚀 Open Notes App",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])

    await update.message.reply_text(
        "Welcome 👋\nOpen your notes app below:",
        reply_markup=keyboard
    )

async def web_app_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = json.loads(update.message.web_app_data.data)

    if data.get("event") == "save":
        await update.message.reply_text("✅ Note saved")
    elif data.get("event") == "export":
        await update.message.reply_text("📦 Backup received")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_handler)
    )

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
