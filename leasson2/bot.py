import os
import ephem
import logging
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

what_day = datetime.datetime.now()


def get_planet(bot, update, args):
    text = args[0]
    planet = getattr(ephem, text)
    planet = planet(what_day)
    planet = ephem.constellation(planet)
    update.message.reply_text(planet[1])


def word_count(bot, update, args):
    if args[0].startswith('"') and args[-1].endswith('"'):
        len_word = len(args)
        update.message.reply_text(len_word)


def calc(bot, update, args):
    element_a = int(args[0].strip())
    usr_operation = args[1]
    element_b = int(args[-1].strip())
    lambda_operation = {
        '-': lambda a, b: a - b,
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b}
    operation = lambda_operation.get(usr_operation)
    if element_a == 0 or element_b == 0:
        update.message.reply_text('division by zero')
    else:
        calcula = operation(element_a, element_b)
        update.message.reply_text(calcula)


def gross(bot, update, args):
    calc = 18 * (1 / 100) * args
    resultat = args - calc
    update.message.reply_text(resultat)


def main():
    key = os.getenv('telegram_key', ' ')
    mybot = Updater(key, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('calc', calc, pass_args=True))
    dp.add_handler(CommandHandler('gross', gross, pass_args=True))
    dp.add_handler(CommandHandler('planet', get_planet, pass_args=True))
    dp.add_handler(CommandHandler('wordcount', word_count, pass_args=True))
    mybot.start_polling()
    mybot.idle()


main()
