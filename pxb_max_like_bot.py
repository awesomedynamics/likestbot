TOKEN = "493667230:AAF8OgeD0HdWUOCQLT0-CWCcQNYPxMMO72I"

import requests


def echo(bot, update):
    text = update.message.text

    keywords = [x for x in text.split()]

    keywords_joined_by_plus = "+".join(keywords)

    r = requests.get('https://pixabay.com/api/?key=7234012-1b25c5b3a2918fa28203f8c24&q=' + keywords_joined_by_plus)

    json_dictionary = r.json()

    global like_dict
    like_dict = {}
    for image_dict in json_dictionary['hits']:
        like_dict[image_dict['likes']] = image_dict['webformatURL']
    url = like_dict.pop(max(like_dict))
    update.message.reply_text(url)

    # list_of_urls.append(image_dict['webformatURL'])

    #for i, url in enumerate(list_of_urls):
        # response = requests.get(url)
        # binary_image = response.content
        # filename = keywords_joined_by_plus + str(i) + ".jpg"
        # with open(filename, "wb") as file:
        #     file.write(binary_image)
        #
        #
        # with open(filename,'rb') as file:
        #     update.message.reply_photo(file)
        #update.message.reply_text(url)
    # update answer
  #  update.message.reply_text(answer)


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
updater = None
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('type your keywords')
def nextpic(bot, update):
    url = like_dict.pop(max(like_dict))
    update.message.reply_text(url)
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
    dp.add_handler(CommandHandler("nextpic", nextpic))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    # log all errors
    dp.add_error_handler(error)
prepare()
updater.start_polling()
updater.idle()