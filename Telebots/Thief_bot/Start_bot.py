import telebot
bot = telebot.TeleBot( "917002472:AAGiOuSM_t0NzDgd3VQYmZecfI7TjYRZiZk" )
class Some_Info():
    var_01 = None
gollum = Some_Info()
print(gollum.var_01)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to( message, "Зря ты сюда зашел" )

@bot.message_handler( content_types=['text'] )
def send_message_1(message):
    User_text = str(message.text)

    if "Код" in User_text:
        gollum.var_01= str(User_text[4:])
        answer  = "Код " + gollum.var_01
        f = open("Start.txt", "w+")
        f.write(gollum.var_01)
    elif "+" in User_text:
        gollum.var_01= str(User_text[2:])
        answer  = "Операция началась " + gollum.var_01
        f = open("Phone.txt", "w+")
        f.write(gollum.var_01)
    else:
        answer = "Я такого еще незнаю"
    bot.send_message( message.chat.id, answer)



bot.polling( none_stop=True )



