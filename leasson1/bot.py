import os
import ephem
import logging
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 
                                  'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

what_day = datetime.datetime.now()

def get_planet(bot, update):
    planet = getattr(ephem, update)
    planet = ephem.constellation(planet(what_day))
    update.message.reply_text(planet[1])


def main():
    key = os.getenv('telegram_key', ' ')
    mybot = Updater(key, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()
