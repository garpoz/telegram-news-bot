#! /usr/bin/python
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from config import token
from telegram import bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler,
)
import telegram, time, hashlib, sqlite3, datetime, os
from telegram import (
    Update,
    ForceReply,
    Sticker,
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
import json
import logging
from telegram import Update, ForceReply

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
up_titr, titr, cap, img = range(4)
in_data = {}


def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("عملیات لغو شد😞")
    return ConversationHandler.END


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        rf"Hi {user.mention_markdown_v2()}\!",
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "/start راه اندازی ربات💡\n\n/help راهنما💡\n\n/begin شروع به کار💡\n\n/cancel لغو عملیات💡\n\n\tتذکر: هر بخشی که میخواهید متن خالی باشد نقطه بگذارید"
    )


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("چنین دستوری وجود ندارد🚫")


def begin(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("رو تیتر را وارد کنید یا نقطه بگذارید📖")
    return up_titr


def UP_TITR(update: Update, context: CallbackContext) -> None:
    if (update.message.text == "/cancel") | (update.message.text == None):
        update.message.reply_text("عملیات لغو شد😞")
        return ConversationHandler.END

    in_data["text_up_titr"] = update.message.text
    update.message.reply_text("تیتر را وارد کنید یا نقطه بگذارید📖")
    return titr


def TITR(update: Update, context: CallbackContext) -> None:
    if (update.message.text == "/cancel") | (update.message.text == None):
        update.message.reply_text("عملیات لغو شد😞")
        return ConversationHandler.END

    in_data["text_titr"] = update.message.text
    update.message.reply_text("کپشن را وارد کنید یا نقطه بگذارید📖")
    return cap


def CAP(update: Update, context: CallbackContext) -> None:
    if (update.message.text == "/cancel") | (update.message.text == None):
        update.message.reply_text("عملیات لغو شد😞")
        return ConversationHandler.END

    in_data["text_cap"] = update.message.text
    update.message.reply_text("یک تصویر وارد کنید. الزامی است🖼️")
    return img


def IMG(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/cancel":
        update.message.reply_text("عملیات لغو شد😞")
        return ConversationHandler.END

    try:
        ifile = update.message.photo[-1].get_file()
        if ifile.file_path[-3:] not in ("jpgpngjpegbmp"):
            update.message.reply_text("لطفا یک تصویر استاندارد انتخاب کنید🖼️")
        else:
            path = ifile.download("input.png")
            update.message.reply_text("با موفقیت انجام شد👍")
            if in_data["text_up_titr"] == ".":
                in_data["text_up_titr"] = ""
            if in_data["text_titr"] == ".":
                in_data["text_titr"] = ""
            if in_data["text_cap"] == ".":
                in_data["text_cap"] = ""
            os.system("convert input.png -resize 1080x1080\! input.png;convert input.png filter.png -gravity center -composite input.png")
            update.message.reply_text("⏳ در حال ساخت و ارسال تصویر نهایی...")
            return ConversationHandler.END
    except:
        update.message.reply_text("لطفا یک تصویر استاندارد انتخاب کنید🖼️")


def main() -> None:
    updater = Updater(f"{token}")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("begin", begin)],
        states={
            up_titr: [MessageHandler(Filters.all, UP_TITR)],
            titr: [MessageHandler(Filters.all, TITR)],
            cap: [MessageHandler(Filters.all, CAP)],
            img: [MessageHandler(Filters.all, IMG)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
