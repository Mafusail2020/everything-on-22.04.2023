import pytube
import telebot
from telebot import types
import os
from threading import *
from time import sleep


banned_sym = "<>/\\|?*\""


def download_music(url: str, chat_id):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_audio_only()
    music_name = youtube.title.strip()
    for sym in banned_sym:
        music_name = music_name.replace(sym, "")
    music_name += ".mp3"
    video.download('C:/Users/krutk/Desktop/Musics temp', filename=music_name)
    try:
        with open(f'C:/Users/krutk/Desktop/Musics temp/{music_name}', 'rb') as file:
            bot.send_audio(chat_id, file)
    except Exception as e:
        bot.send_message(chat_id, f"Sorry, some errors occured while downloading {music_name}")
        print(e)
    finally:
        os.remove(f"C:/Users/krutk/Desktop/Musics temp/{music_name}")


def download_video(url: str, chat_id):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    music_name = youtube.title.strip()
    for sym in banned_sym:
        music_name = music_name.replace(sym, "")
    music_name += ".mp4"
    video.download('C:/Users/krutk/Desktop/Musics temp', filename=music_name)
    try:
        with open(f'C:/Users/krutk/Desktop/Musics temp/{music_name}', 'rb') as file:
            bot.send_video(chat_id, file)
    except Exception as e:
        bot.send_message(chat_id, f"Sorry, some errors occured while downloading {music_name}")
        print(e)
    finally:
        os.remove(f"C:/Users/krutk/Desktop/Musics temp/{music_name}")


token = "5592855337:AAFaapt8Cm1DNtCwslxjpkeCURLKxjrLaoA"
bot = telebot.TeleBot(token)
parse_mode = "m"


@bot.message_handler(commands=["start"])
def start(mes: types.Message):
    cb = types.InlineKeyboardMarkup()
    cb.row(types.InlineKeyboardButton(text="Convert to mp3 file🎵️ ", callback_data="pm_m"),
           types.InlineKeyboardButton(text="▶️ Convert to mp4 file", callback_data="pm_v"))

    bot.send_message(mes.chat.id, """Welcome to the YouTube music bot
    You can send a link to the video, and it simply will download
    an audio from this video
But if you need to download the video you can switch downloading mode with help of two buttons below""",
                     reply_markup=cb)


@bot.callback_query_handler(func=lambda callback: callback.data.startswith("pm"))
def set_parse_mode(callback: types.CallbackQuery):
    global parse_mode
    parse_mode = callback.data.split("_")[1]
    if parse_mode == 'm':
        bot.send_message(callback.message.chat.id, "Downloading mode was changed to music")
    else:
        bot.send_message(callback.message.chat.id, "Downloading mode was changed to video")


# This function handles links and then gives them to download function
@bot.message_handler(content_types=['text'])
def handler(mes: types.Message):
    url_list = mes.text.split()
    thread_lst = []

    if parse_mode == 'm':
        bot.send_message(mes.chat.id, "Download has started, we will inform you when download is ready...")

        for url in url_list:
            thread = Thread(target=download_music, args=(url, mes.chat.id))
            thread_lst.append(thread)
            thread.start()

        while any(thread.is_alive() for thread in thread_lst):
            sleep(2)

        bot.send_message(mes.chat.id, "Download finished! Thanks for using")

    elif parse_mode == 'v':
        bot.send_message(mes.chat.id, "Download has started, we will inform you when download is ready...")

        for url in url_list:
            thread = Thread(target=download_video, args=(url, mes.chat.id))
            thread_lst.append(thread)
            thread.start()

        while any(thread.is_alive() for thread in thread_lst):
            sleep(2)

        bot.send_message(mes.chat.id, "Download finished! Thanks for using")


bot.polling(none_stop=True)
