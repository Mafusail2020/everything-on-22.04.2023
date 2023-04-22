import telebot

Token = "5480010898:AAHk3NNfod0J3Thh9w8S3rRuBVmDS-I3bgI"
bot = telebot.TeleBot(Token)


@bot.message_handler(content_types=['document', 'audio', 'video', 'text', 'photo'])
def send(mes: telebot.types.Message):
    fileid = None
    file_type = None

    try:

        bot.send_message(mes.chat.id, mes.document.file_id)
        print("Document")
        fileid = mes.document.file_id
        file_type = mes.document.file_id
    except AttributeError:
        try:
            bot.send_message(mes.chat.id, mes.video.file_id)
            print("Video")
            fileid = mes.video.file_id
            file_type = mes.video.file_name
        except AttributeError:
            try:

                bot.send_message(mes.chat.id, mes.audio.file_id)
                print("Audio")
                fileid = mes.audio.file_id
                file_type = mes.audio.file_name
            except AttributeError:
                try:

                    bot.send_message(mes.chat.id, mes.voice.file_id)
                    print("Voice")
                    fileid = mes.voice.file_id
                    file_type = "Voice.mp4"
                except AttributeError:

                    bot.send_message(mes.chat.id, mes.photo[0].file_id)
                    print("Photo")
                    fileid = mes.photo[0].file_id
                    file_type = "???.png"

    file_info = bot.get_file(fileid)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_type, 'wb') as new_file:
        new_file.write(downloaded_file)


bot.polling(non_stop=True)
