#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import jdatetime
import datetime
from ECG.models import Patient, Report
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from djqscsv import render_to_csv_response, write_csv

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('This is a test robot for ECG sensor in hospital')


def help(update, context):
    update.message.reply_text('/t/jalali-jalali date in form of year/month/date\n/n/patient number')


def message(update, context):
    """Echo the user message."""
    text = update.message.text
    chat_id = update.message.chat_id
    if text[1] == 't':
        Date_Year1 = text[3:7]
        Date_Month1 = text[8:10]
        Date_Day1 = text[11:13]
        Date_Year2 = text[14:18]
        Date_Month2 = text[19:21]
        Date_Day2 = text[22:24]
        date1 = jdatetime.date(int(Date_Year1),int(Date_Month1),int(Date_Day1)).togregorian()
        date2 = jdatetime.date(int(Date_Year2),int(Date_Month2),int(Date_Day2)).togregorian()
        reports = Report.objects.filter(create_date__gte = date1, create_date__lte = date2)
        with open('file.csv', 'wb') as csv_file:
            write_csv(reports, csv_file)
        context.bot.sendDocument(document=open('file.csv', 'rb'), chat_id=chat_id)
        
    if text[1] == 'n':
        patient_number = int(text[3:])
        patient = Patient.objects.get(patient_number=patient_number)
        reports = Report.objects.filter(patient=patient)
        with open('file.csv', 'wb') as csv_file:
            write_csv(reports, csv_file)
        context.bot.sendDocument(document=open('file.csv', 'rb'), chat_id=chat_id)



def run():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5181733554:AAFDEJlQpcZWVGDjvX28NTelwqSgVeNEB9U", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


