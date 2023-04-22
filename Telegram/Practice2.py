import telebot
from telebot import types


token = "6168121228:AAFyHRGFoT72qFCnBx6brK0l-aQXIOmkVgE"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(msg):
    inl = types.InlineKeyboardMarkup()
    inls = [("BRUH", 'br')]
    for text, clb in inls:
        inl.add(types.InlineKeyboardButton(text=text, callback_data=clb))

    rmk = types.ReplyKeyboardMarkup().add("/Menu")

    bot.send_message(msg.chat.id, "Sup, amogus?", reply_markup=inl)
    bot.send_message(msg.chat.id, "Sus!", reply_markup=rmk)


@bot.callback_query_handler(func=lambda clb: clb.data.startswith('br'))
def br(mes):
    bot.send_message(mes.message.chat.id, "DICK")


@bot.message_handler(commands=['Menu'])
def mune(msg):
    repl = bot.send_message(msg.chat.id, "wot u want?")
    bot.register_next_step_handler(repl, s2)


def s2(mes):
    bot.send_message(mes.chat.id, text=mes.text)



bot.polling(none_stop=True)
