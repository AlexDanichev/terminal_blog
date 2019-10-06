import telebot
bot = telebot.TeleBot( "917002472:AAGiOuSM_t0NzDgd3VQYmZecfI7TjYRZiZk" )


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to( message, "Привет, это бот который напоминает тебе что Саша тебя любит \n"
                           "напиши про кого ты хочешь узнать" )

@bot.message_handler( content_types=['text'] )
def send_message_1(message):
    User_text = str(message.text)
    if User_text == "Винни":
        answer = "Маленькикй милый шпиц, гоняет котов"

    elif User_text == "Саша":
        answer = "Глупый топсяк толстяк"
    elif User_text == "Маша":
        answer = "УРУРУРУРРУРУРУ"
    elif User_text == "Машенька":
        answer = "УРУРУРУРРУРУРУ"
    elif User_text == "Кот":
        answer = "Брющик его имя, кушать еду и греть Марину его предназначение"
    elif User_text == "Котис":
        answer = "Брющик его имя, кушать еду и греть Марину его предназначение"
    elif User_text == "Ник":
        answer = "Брющик его имя, кушать еду и греть Марину его предназначение"
    else:
        answer = "Я такого еще незнаю"
    bot.send_message( message.chat.id, answer)


bot.polling( none_stop=True )



