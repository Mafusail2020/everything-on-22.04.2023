import telebot
from telebot import types


token = "6168121228:AAFyHRGFoT72qFCnBx6brK0l-aQXIOmkVgE"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    inl = types.InlineKeyboardMarkup(row_width=2)
    btns = [("Left", "left"), ("Right", "right")]

    for btn, clb in btns:
        inl.add(types.InlineKeyboardButton(text=btn, callback_data=clb))

    btns = ["/Menu", "/Bin"]
    rmk = types.ReplyKeyboardMarkup()
    for btn in btns:
        rmk.add(btn)

    bot.send_message(msg.chat.id, "Practice lul", reply_markup=inl)
    bot.send_message(msg.chat.id, "Yoy", reply_markup=rmk)


@bot.message_handler(commands=['Bin'])
def bbin(msg: types.Message):
    bot.send_message(msg.chat.id, "BIN.")


@bot.message_handler(commands=['Menu'])
def menu(msg: types.Message):
    answ = bot.send_message(msg.chat.id, "Yo pizza or burger")
    bot.register_next_step_handler(answ, menu2)


def menu2(msg: types.Message):
    bot.send_message(msg.chat.id, text=msg.text)


@bot.callback_query_handler(func=lambda clb: clb.data.startswith("left"))
def left(clb: types.CallbackQuery):
    bot.send_message(clb.message.chat.id, f"You pressed {clb.data}!")


@bot.callback_query_handler(func=lambda clb: clb.data.startswith("right"))
def left(clb: types.CallbackQuery):
    bot.send_message(clb.message.chat.id, f"You pressed {clb.data}!")


bot.polling(none_stop=True)