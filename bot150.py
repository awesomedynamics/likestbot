TOKEN = "491593727:AAHUC7wZSEkcAu3Kbb6vrHDYyhue8R_-ntw"
def echo(bot, update):
    answer =  "nol"
    text = update.message.text

    if "300" in text or "триста" in text or "з00" in text or "зоо" in text or "Зоо" in text or "Триста" in text:
        answer = "отсоси у тракториста"
    elif text == "нет" or text == "Нет" or text[-3:] == "нет":
        answer = "пидора ответ"
    elif text[-2:] == "да" or text[-2:] == "Да":
        answer = "пизда"
    elif "где" in text or "Где" in text:
        answer = "в пизде"
    elif text == "три сотни" or  text == "Три сотни":
        answer = "а ты норм"
    elif text[-3:-1] == "ты" or text[-2:] == "Ты" or text[-2:] == "ты":
        answer = "жопой нюхаешь цветы"
    else:
        pass
    # update answer
    if answer != "nol":
        update.message.reply_text(answer)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
updater = None
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('сколько будет 150+150?!')
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
def prepare():
    """Start the bot."""
    global updater
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    # log all errors
    dp.add_error_handler(error)
prepare()
updater.start_polling()
updater.idle()