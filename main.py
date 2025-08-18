import os
import telebot
from keep_alive import keep_alive

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot is running 24/7 on Replit!")

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, "🛑 Bot stopped!")

keep_alive()
bot.polling()
