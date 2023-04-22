import requests
import telebot
from telebot import types


id_Nekita = "856343001"
id_Misha = "0000"

Token = "5480010898:AAHk3NNfod0J3Thh9w8S3rRuBVmDS-I3bgI"
chat_id = "1041740008"
bot = telebot.TeleBot(Token)
requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={chat_id}&text=Launched")


@bot.message_handler(commands=['start'])
def start(mes):
    if mes.chat.id == 1041740008:
        variants = ["/Nekit", "/Misha"]

        kbmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in variants:
            kbmk.add(i)
        bot.send_message(mes.chat.id, "Кому отослать сообщение?", reply_markup=kbmk)


@bot.message_handler(['Nekit'])
def nekit(mes):
    msg = bot.send_message(mes.chat.id, "Что отправить некиту?")
    bot.register_next_step_handler(msg, nek)


def nek(mes):
    bot.send_message(id_Nekita, mes.text)


@bot.message_handler(['Nekit'])
def misha(mes):
    msg = bot.send_message(mes.chat.id, "Что отправить Михе?")
    bot.register_next_step_handler(msg, nek)


def mish(mes):
    bot.send_message(id_Misha, mes.text)


bot.polling(non_stop=True)
