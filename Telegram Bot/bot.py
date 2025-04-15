import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils import load_data, save_data, get_balance_summary, ensure_user

logging.basicConfig(level=logging.INFO)

DATA_FILE = "data.json"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to your Financial Planner Bot!\nUse /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📌 Available Commands:
/start - Start the bot
/help - Show help info
/config - Set income or category budget
/log - Log income or expense
/summary - Show current balance and budgets
/notifyon - Enable notifications
/notifyoff - Disable notifications
""")

async def config(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()
    user_id = str(update.message.from_user.id)
    ensure_user(data, user_id)

    try:
        category = context.args[0].lower()
        amount = float(context.args[1])
        if category == "income":
            data[user_id]["income"] = amount
            await update.message.reply_text(f"✅ Income set to ${amount:.2f}")
        else:
            data[user_id]["budgets"][category] = amount
            await update.message.reply_text(f"✅ Budget for '{category}' set to ${amount:.2f}")
        save_data(data)
    except:
        await update.message.reply_text("❌ Usage: /config [category|income] [amount]")

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()
    user_id = str(update.message.from_user.id)
    ensure_user(data, user_id)

    try:
        amount = float(context.args[0])
        category = context.args[1]
        type_ = "expense" if amount < 0 else "income"
        data[user_id]["transactions"].append({
            "amount": amount,
            "category": category,
            "type": type_
        })
        save_data(data)
        await update.message.reply_text(f"✅ Logged {type_}: ${amount} in '{category}'")
    except:
        await update.message.reply_text("❌ Usage: /log [amount] [category]")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()
    user_id = str(update.message.from_user.id)
    ensure_user(data, user_id)

    summary_text = get_balance_summary(data[user_id])
    await update.message.reply_text(summary_text)

async def notify_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()
    user_id = str(update.message.from_user.id)
    ensure_user(data, user_id)

    data[user_id]["notifications"] = True
    save_data(data)
    await update.message.reply_text("🔔 Daily notifications enabled.")

async def notify_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()
    user_id = str(update.message.from_user.id)
    ensure_user(data, user_id)

    data[user_id]["notifications"] = False
    save_data(data)
    await update.message.reply_text("🔕 Notifications disabled.")

if __name__ == '__main__':
    with open("token.txt") as f:
        TOKEN = f.read().strip()
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("config", config))
    app.add_handler(CommandHandler("log", log))
    app.add_handler(CommandHandler("summary", summary))
    app.add_handler(CommandHandler("notifyon", notify_on))
    app.add_handler(CommandHandler("notifyoff", notify_off))

    app.run_polling()
