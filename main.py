from telegram import *
from telegram.ext import *
import os

from Modules.Messages.message import msg

message = msg()

TOKEN = "5516328242:AAGtqBTVcfnrtIB7CMa4EmM_Wc6FBKL607c"
PORT = int(os.environ.get('PORT', 443))

def main():
    """Start the bot."""

    updater = Updater(
        TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", msg.welcomeMsg))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, message.response))

    # Start the Bot
    updater.start_webhook(listen='0.0.0.0',
                            port=PORT,
                            url_path=TOKEN,
                            webhook_url='https://joli-croissant-99758.herokuapp.com/' + TOKEN)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)

    updater.idle()


if __name__ == '__main__':
    main()
