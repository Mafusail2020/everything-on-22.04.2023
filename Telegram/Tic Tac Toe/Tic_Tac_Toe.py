import telebot
from telebot import types
import requests
from Game import TicTacToeSolo, TicTacToeMult

# ДОБАВИТЬ ЧАТ
game_solo = TicTacToeSolo()
game_mult = TicTacToeMult()

user1 = ""
user2 = ""
isUser1Turn = True

token = "5788539136:AAGac2fiLHtDG13u9r2mIMgvGN01tbXabuY"
chat_id = "1041740008"
bot = telebot.TeleBot(token)
requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=TicTacToe")


# Show pole for solo game
def show_pole_solo(callback):
    inline = types.InlineKeyboardMarkup()
    inline.row(types.InlineKeyboardButton(text="↖️", callback_data="solo_0_0"),
               types.InlineKeyboardButton(text="⬆️", callback_data="solo_0_1"),
               types.InlineKeyboardButton(text="↗️", callback_data="solo_0_2")).row(
        types.InlineKeyboardButton(text="⬅️", callback_data="solo_1_0"),
        types.InlineKeyboardButton(text="⏺️", callback_data="solo_1_1"),
        types.InlineKeyboardButton(text="➡️", callback_data="solo_1_2")
    ).row(types.InlineKeyboardButton(text="↙️", callback_data="solo_2_0"),
          types.InlineKeyboardButton(text="⬇️", callback_data="solo_2_1"),
          types.InlineKeyboardButton(text="↘️", callback_data="solo_2_2"))
    bot.send_message(callback.message.chat.id, f"""{game_solo.return_pole()}

        Choose a cell to set the X!""", reply_markup=inline)


# Show pole in mult
def show_pole(user1_id, user2_id):
    global isUser1Turn

    if isUser1Turn:
        inline = types.InlineKeyboardMarkup()
        inline.row(types.InlineKeyboardButton(text="↖️", callback_data="mult_0_0_x"),
                   types.InlineKeyboardButton(text="⬆️", callback_data="mult_0_1_x"),
                   types.InlineKeyboardButton(text="↗️", callback_data="mult_0_2_x")).row(
            types.InlineKeyboardButton(text="⬅️", callback_data="mult_1_0_x"),
            types.InlineKeyboardButton(text="⏺️", callback_data="mult_1_1_x"),
            types.InlineKeyboardButton(text="➡️", callback_data="mult_1_2_x")
        ).row(types.InlineKeyboardButton(text="↙️", callback_data="mult_2_0_x"),
              types.InlineKeyboardButton(text="⬇️", callback_data="mult_2_1_x"),
              types.InlineKeyboardButton(text="↘️", callback_data="mult_2_2_x"))
        bot.send_message(user1_id, f"""{game_mult.return_pole()}

                Choose a cell to set the X!""", reply_markup=inline)
        isUser1Turn = not isUser1Turn
    else:
        inline = types.InlineKeyboardMarkup()
        inline.row(types.InlineKeyboardButton(text="↖️", callback_data="mult_0_0_o"),
                   types.InlineKeyboardButton(text="⬆️", callback_data="mult_0_1_o"),
                   types.InlineKeyboardButton(text="↗️", callback_data="mult_0_2_o")).row(
            types.InlineKeyboardButton(text="⬅️", callback_data="mult_1_0_o"),
            types.InlineKeyboardButton(text="⏺️", callback_data="mult_1_1_o"),
            types.InlineKeyboardButton(text="➡️", callback_data="mult_1_2_o")
        ).row(types.InlineKeyboardButton(text="↙️", callback_data="mult_2_0_o"),
              types.InlineKeyboardButton(text="⬇️", callback_data="mult_2_1_o"),
              types.InlineKeyboardButton(text="↘️", callback_data="mult_2_2_o"))
        bot.send_message(user2_id, f"""{game_mult.return_pole()}

                        Choose a cell to set the O!""", reply_markup=inline)
        isUser1Turn = not isUser1Turn


@bot.message_handler(commands=['start'])
def start(mes: types.Message):
    db = open("Users.txt", encoding="utf-8")

    user_not_in_db = True
    user_name = None

    for user in db.readlines():
        us_id = user.split()[0]

        if us_id == str(mes.chat.id):
            user_not_in_db = False
            user_name = user.split()[1]

    if user_not_in_db:
        bot.send_message(mes.chat.id, "Welcome, please follow /instructions to register on TicTacToe")
        add_user_id = open("Users.txt", "a", encoding="utf-8")
        add_user_id.write(f"{mes.chat.id} {mes.chat.first_name}\n")

        add_user_id.close()
    else:
        button_text = ["Statistics", "Challenge", "Solo game"]
        button_func = ["show_stats", "send_battle_req", "start_solo_game"]

        buttons = zip(button_text, button_func)
        inline = types.InlineKeyboardMarkup()
        for text, data in buttons:
            button = types.InlineKeyboardButton(text=text, callback_data=data)
            inline.add(button)
        bot.send_message(mes.chat.id, f"Nice to see you again, {user_name}, what would you like to do?",
                         reply_markup=inline)

    db.close()


# Showing users statistics
@bot.callback_query_handler(func=lambda callback: callback.data.startswith("show_stats"))
def show_stats(callback: types.CallbackQuery):
    bot.send_message(callback.message.chat.id, "Stats")


# Starting solo game with a bot
@bot.callback_query_handler(func=lambda callback: callback.data.startswith("start_solo_game"))
def show_stats(callback: types.CallbackQuery):
    bot.send_message(callback.message.chat.id, "Solo game starts now!")

    show_pole_solo(callback)


# Solo game code
@bot.callback_query_handler(func=lambda callback: callback.data.startswith("solo"))
def solo(callback: types.CallbackQuery):
    bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id)
    row, col = callback.data[-3:].split("_")
    row, col = int(row), int(col)

    if game_solo.is_x_valid(row, col):
        who_won = game_solo.set_x(row, col)
        if who_won != "":
            if who_won == "X":
                bot.send_message(callback.message.chat.id, f"{game_solo.return_pole()}")
                bot.send_message(callback.message.chat.id, f"Congrats! you won!")
            else:
                bot.send_message(callback.message.chat.id, f"{game_solo.return_pole()}")
                bot.send_message(callback.message.chat.id, f"Welp, maybe next time!")
        else:
            show_pole_solo(callback)
    else:
        bot.send_message(callback.message.chat.id, "This cell is occupied!")
        show_pole_solo(callback)


# Multiplayer game code
@bot.callback_query_handler(func=lambda callback: callback.data.startswith("send_battle_req"))
def multiplayer(callback: types.CallbackQuery):
    users_db = open("Users.txt", encoding='utf-8')
    us = []
    rmk = types.ReplyKeyboardMarkup()
    for user in users_db:
        us.append(user.split()[1])

    for u in us:
        rmk.add(u)

    msg = bot.send_message(callback.message.chat.id, "Battle", reply_markup=rmk)
    bot.register_next_step_handler(msg, mult)

    users_db.close()


def mult(msg: types.Message):
    global user1, user2
    user1 = msg.chat.id
    user_db = open("Users.txt", encoding="utf-8")

    for user in user_db:
        if user.split()[1] == msg.text:
            user2 = user.split()[0]

    show_pole(user1, user2)


@bot.callback_query_handler(func=lambda callback: callback.data.startswith("mult"))
def mult_turn(callback: types.CallbackQuery):
    global user1, user2, isUser1Turn
    "mult_1_0_o"
    _, row, col, value = callback.data.split("_")
    row, col, value = int(row), int(col), str(value)
    bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id)

    # bot.send_message(user1, f"row: {row}, col: {col}, value: {value}")

    if value.lower() == "x":
        if game_mult.is_cell_valid(row, col):
            game_mult.set_x(row, col)
            if game_mult.is_win():
                bot.send_message(user2, f"{game_mult.return_pole()}")
                bot.send_message(user1, f"{game_mult.return_pole()}")
                bot.send_message(user1, "Player 1 (X) won!!!!")
                bot.send_message(user2, "Player 1 (X) won!!!!")
                game_mult.clear()
                return
        else:
            bot.send_message(callback.message.chat.id, "Cell is occupied! Choose another!")
            isUser1Turn = not isUser1Turn

    else:
        if game_mult.is_cell_valid(row, col):
            game_mult.set_o(row, col)
            if game_mult.is_win():
                bot.send_message(user2, f"{game_mult.return_pole()}")
                bot.send_message(user1, f"{game_mult.return_pole()}")
                bot.send_message(user1, "Player 2 (O) won!!!!")
                bot.send_message(user2, "Player 2 (O) won!!!!")
                game_mult.clear()
                return
        else:
            bot.send_message(callback.message.chat.id, "Cell is occupied! Choose another!")
            isUser1Turn = not isUser1Turn

    if game_mult.is_tie():

        bot.send_message(user2, f"{game_mult.return_pole()}")
        bot.send_message(user1, f"{game_mult.return_pole()}")
        bot.send_message(user1, "Tie!!!!")
        bot.send_message(user2, "Tie!!!!")

        game_mult.clear()
        return

    bot.send_message(callback.message.chat.id, f"{game_mult.return_pole()}")

    show_pole(user1, user2)


bot.polling(none_stop=True)
