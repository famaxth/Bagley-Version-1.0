#Production by Berlin
#Telegram - @por0vos1k

# -*- coding: utf-8 -*-

import telebot
import config
import time
import random
from time import sleep

bot = telebot.TeleBot(config.token, parse_mode='HTML')
print("Start")


def save_name(message):
    f = open('name_user.txt', 'w')
    f.write(message.text)
    bot.send_message(message.chat.id, config.texts['name_1'])
    time.sleep(2)
    bot.send_message(message.chat.id, config.texts['name_2'])


@bot.message_handler(commands=['start'])
def start(message):
    text = bot.send_message(message.chat.id, config.texts['start'])
    bot.register_next_step_handler(text, save_name)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text.lower() in config.hello:
        text = random.choice(config.hello_answer)
        bot.send_message(message.chat.id, text)
    elif message.text.lower() in config.hello_answer:
        text = random.choice(config.hello_answer)
        bot.send_message(message.chat.id, text)
    elif message.text.lower() in config.angry_hello:
        text = random.choice(config.angry_hello_answer)
        bot.send_message(message.chat.id, text)
    elif message.text.lower() in config.lock_1:
        text = random.choice(config.lock_1_answer)
        bot.send_message(message.chat.id, text)
    elif message.text.lower() in config.how_are_you:
        text = random.choice(config.how_are_you_answer)
        bot.send_message(message.chat.id, text)



if __name__ == '__main__':
    bot.polling(none_stop=True)