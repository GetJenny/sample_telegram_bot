#####!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.


import sys
import time
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import starchat_interface as starchat_interface

starchat = starchat_interface.Starchat()
starchat.starchat_url = "http://localhost:8888"
starchat.post_headers = {'Content-Type': 'application/json'}
starchat.get_headers = starchat.post_headers


"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)

# a basic datastore for session informations
datastore = {}


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    data = {
        "user_first_name": update.message.chat.first_name
    }
    body = {
        "conversation_id": str(update.message.chat_id),
        "user_input": { "text": "" },
        "values": {
            "return_value": "init",
            "traversed_states": [],
            "data": data
        }
    }

    bot.sendMessage(update.message.chat_id, text='Hello,\n', parse_mode="HTML")
    try:
        res = starchat.get_next_response(body=body)
        logger.debug(res)
        response = res[1][0]["bubble"]
        datastore[update.message.chat_id] = {"traversed_states": res[1][0]["traversed_states"], "data": data}
        bot.sendMessage(update.message.chat_id, text=response, parse_mode="HTML")
    except starchat_interface.ApiCallException as e:
        response = "I'm sorry " + update.message.chat.first_name +\
                   ", a problem occourred, please try later or type /help to get the available commands"
        logger.error(e.value)
        bot.sendMessage(update.message.chat_id, text=response, parse_mode="HTML")
    except KeyError as e:
        response = "I'm sorry " + update.message.chat.first_name + ", I don't know how to answer, sorry"
        logger.error(e.value)
        bot.sendMessage(update.message.chat_id, text=response, parse_mode="HTML")
    except IndexError as e:
        response = "I'm sorry " + update.message.chat.first_name + ", I don't know how to answer, sorry"
        logger.error(e.value)
        bot.sendMessage(update.message.chat_id, text=response, parse_mode="HTML")


def echo(bot, update):

    try:
        data = datastore[update.message.chat_id]["data"]
        traversed_states = datastore[update.message.chat_id]["traversed_states"]
    except:
        data = { "user_first_name": update.message.chat.first_name }
        traversed_states = []

    body = {
            "conversation_id": str(update.message.chat_id),
            "user_input": {
                "text": update.message.text
            },
            "data": data,
            "traversed_states": traversed_states
        }

    try:
        res = starchat.get_next_response(body=body)
        logger.debug(res)
        response = res[1][0]["bubble"]
        bot.sendMessage(update.message.chat_id, text=response, parse_mode="HTML")
        datastore.setdefault(update.message.chat_id, {})["traversed_states"] = res[1][0]["traversed_states"]
        datastore[update.message.chat_id]["data"] = res[1][0]["data"]
        print("DATASTORE>>>> ", datastore)
    except (starchat_interface.NoContentApiCallException, KeyError, IndexError) as e:
        response = "I'm sorry " + update.message.chat.first_name + ", I don't know how to answer"
        logger.error(e.value)
        bot.sendMessage(update.message.chat_id, text=response, parse_mode="HTML")
    except starchat_interface.ApiCallException as e:
        response = "I'm sorry " + update.message.chat.first_name +\
                   ", a problem occourred, please try later or type /help to get the available commands"
        logger.error(e.value)
        bot.sendMessage(update.message.chat_id, text=response, parse_mode="HTML")


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("XXXX")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
