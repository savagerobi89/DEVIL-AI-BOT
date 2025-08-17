import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

active_users = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    active_users.add(user_id)
    await update.message.reply_text("✅ Signal শুরু হয়েছে! আপনি এখন সিগনাল পাবেন।")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    if user_id in active_users:
        active_users.remove(user_id)
    await update.message.reply_text("🛑 Signal বন্ধ করা হলো।")

async def send_signal(context: ContextTypes.DEFAULT_TYPE):
    for user_id in list(active_users):
        try:
            await context.bot.send_message(chat_id=user_id, text="📊 নতুন সিগনাল: BUY EUR/USD")
        except Exception as e:
            print(f"Error sending to {user_id}: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))

    # এখানে job_queue সেট করতে হবে
    job_queue = app.job_queue
    job_queue.run_repeating(send_signal, interval=60, first=10)

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
