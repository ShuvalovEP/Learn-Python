import os
import ephem
import logging
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

what_day = datetime.datetime.now()

def talk_to_me(bot, update):
    planet = update.message.text 
    if planet == 'merkury':
        planet = ephem.Mercury(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif planet == 'wenus':
        planet = ephem.Venus(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif update == 'mars':
        planet = ephem.Mars(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif update == 'jupiter':
        planet = ephem.Jupiter(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif update == 'saturn':
        planet = ephem.Saturn(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif planet == 'uran':
        planet = ephem.Uranus(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif planet == 'neptun':
        planet = ephem.Neptune(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif planet == 'pluton':
        planet = ephem.Pluto(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])
    elif planet == 'moon':
        planet = ephem.Moon(what_day)
        planet = ephem.constellation(planet)
        update.message.reply_text(planet[1])


def main():
    key = os.getenv('telegram_key', '')
    mybot = Updater(key, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()
