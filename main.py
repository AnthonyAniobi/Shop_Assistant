# import telebot
from logging import DEBUG
from telebot import types, TeleBot
from config import token
from flask import Flask

bot = TeleBot(token=token)
server = Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing? sucker!")

#block to handle only text messages
@bot.message_handler(func=lambda message:True, content_types=['text'])
def echo_all(message):
    bot.reply_to(message, message.text)
    # bot.send_message(message.text)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('b')
itembtn3 = types.KeyboardButton('v')
markup.add(itembtn1, itembtn2)

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL+TOKEN)


if DEBUG == True:
    bot.remove_webhook()
    bot.polling()
else:
    if __name__ == "__main__":
        server.run(host)