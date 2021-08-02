import os
from logging import DEBUG
import telebot
from config import TOKEN, APP_URL
from fastapi import FastAPI

bot = telebot.TeleBot(TOKEN)
server = FastAPI()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? sucker!")

@bot.message_handler(func=lambda message:True, content_types=['text'])
def echo_all(message):
    bot.reply_to(message, message.text)
    
# @bot.callback_query_handler(func=lambda call:True)
# def message_handler(message):
#     bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_mar
#     kup())

# def gen_markup():
#     markup = types.InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(types.InlineKeyboardButton("Yes", callback_data="cb_yes"), types.InlineKeyboardButton("No", callback_data="cb_no"))
#     return markup

# @bot.message_handler(func=lambda message:True, content_types=types.KeyboardButton)
# def button_click(message):
#     bot.reply_to(message, message.)


# markup = types.ReplyKeyboardMarkup()
# itembtn1 = types.KeyboardButton('a')
# itembtn2 = types.KeyboardButton('b')
# itembtn3 = types.KeyboardButton('c')
# itembtn4 = types.KeyboardButton('d')
# itembtn5 = types.KeyboardButton('e')
# itembtn6 = types.KeyboardButton('f')
# markup.row(itembtn1, itembtn2, itembtn3)
# markup.row(itembtn4, itembtn5, itembtn6)


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL+TOKEN)


if DEBUG == True:
    bot.remove_webhook()
    bot.polling()
else:
    if __name__ == "__main__":
        server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))