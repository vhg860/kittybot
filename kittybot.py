import logging
import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

URL = 'https://api.thecatapi.com/v1/images/search'
URL2 = 'https://api.thedogapi.com/v1/images/search'


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(URL2)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def get_new_image_dog():
    try:
        response = requests.get(URL2)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(URL)
    response = response.json()
    random_dog = response[0].get('url')
    return random_dog


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_dog())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup(
        [['/newcat'], ['/newdog']], resize_keyboard=True
    )

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button
    )
    context.bot.send_photo(chat.id, get_new_image())


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(CommandHandler('newdog', new_dog))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
