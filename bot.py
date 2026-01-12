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

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🔁 CHANGE THIS PER PROJECT
WEB_APP_URL = "https://abrahambekele2090.github.io/telegram-webapp/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🔐 Open App",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])
    await update.message.reply_text(
        "Open your personal app below.",
        reply_markup=keyboard
    )

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = json.loads(update.message.web_app_data.data)
    if data.get("event") == "export":
        await update.message.reply_text("📦 Backup received")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))
app.run_polling()
