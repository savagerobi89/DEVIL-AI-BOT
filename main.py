import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Render এ Environment Variable থেকে Token নিবে

active_users = set()

def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    active_users.add(user_id)
    update.message.reply_text("✅ Signal শুরু হয়েছে! আপনি এখন সিগনাল পাবেন।")

def stop(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    if user_id in active_users:
        active_users.remove(user_id)
    update.message.reply_text("🛑 Signal বন্ধ করা হলো।")

def send_signal(context: CallbackContext):
    for user_id in active_users:
        context.bot.send_message(chat_id=user_id, text="📊 নতুন সিগনাল: BUY EUR/USD")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))

    job_queue = updater.job_queue
    job_queue.run_repeating(send_signal, interval=60, first=10)  # প্রতি ১ মিনিটে Signal পাঠাবে

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
