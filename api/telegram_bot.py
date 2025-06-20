import os
import sys
sys.path.append('C:\\Users\\hp\\Telegram_Bot')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
import django
django.setup()
from decouple import config
import logging
from telegram.ext import Updater, CommandHandler
from api.models import TelegramUser  # Import the model

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')

def start(update, context):
    username = update.message.from_user.username
    if username:
        TelegramUser.objects.get_or_create(username=username)
        update.message.reply_text(f'Welcome, {username}! Your username has been recorded.')
    else:
        update.message.reply_text('Please set a Telegram username in your profile.')

def main():
    try:
        updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('start', start))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logging.error(f"Bot failed: {e}")
        raise

if __name__ == '__main__':
    main()
