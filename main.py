#! /usr/bin/python
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from config import token
from telegram.ext import(
        Updater,
        CommandHandler,
        MessageHandler,
        Filters,
        ConversationHandler,
        CallbackContext,
        CallbackQueryHandler
)
import telegram,time,hashlib,sqlite3,datetime,os
from telegram import Update,ForceReply,Sticker,KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
import json
import logging
from telegram import Update, ForceReply

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
up_titr=range(1)

def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('عملیات لغو شد')
    return ConversationHandler.END

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
    )

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/start راه اندازی ربات\n\n/help راهنما\n\n/begin شروع به کار\n\n/cancel لغو عملیات')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('چنین دستوری وجود ندارد')

def begin(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('رو تیتر را وارد کنید یا خالی بگذارید')
    return up_titr

def UP_TITR(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('تیتر را وارد کنید یا خالی بگذارید')
    return ConversationHandler.END

def main() -> None:
    updater = Updater(f"{token}")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('begin', begin)],
        states={
            up_titr: [MessageHandler(Filters.all, UP_TITR)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
