from gtts import gTTS
import telebot
from pydub import AudioSegment
import time



bot = telebot.TeleBot("708925052:AAEq_Q-BOQUnfwMR2ahLrIRa9EAXSlHG5Jw")
@bot.message_handler( commands=['start', 'help'] )
def send_welcome(message):
    bot.reply_to( message, "Привет, это пробный разговорный бот, отправь"
                           " мне сообщение и я прочитаю его пока буду идти к реке")

@bot.message_handler( content_types=['text'] )
def send_message_1(message):
    user_text = str(message.text)
    user_name = message.from_user.id #Запрашивание имени пользователя
    if len(user_text) > 85:
        answer = "Слишком много текста епта"
    else:
        tts_en = gTTS(user_text, lang='ru')
        with open("{}.mp3".format(user_name), 'wb') as f: #поидее должно сохранять файл под именем пользователя тчтобы избежать дублей
            tts_en.write_to_fp(f)


        bot.send_voice(chat_id=message.chat.id ,voice=open('{}.mp3'.format(user_name), 'rb')) #отправляет мп3 как голосовое сообщение


bot.polling( none_stop=True )


# tts_en = gTTS('Привет епта', lang='ru')
# tts_fr = gTTS('bonjour', lang='fr')
#
# with open('Privet.mp3', 'wb') as f:
#     tts_en.write_to_fp(f)
# x = "третий год не разберут что там в завещании третий год не разберут что там в завещании"
# print(len(x))