import telebot
from telebot import types

bot = telebot.TeleBot( "845062436:AAGs5eU-tp3_moWfFX3dqFBVGSW14QY6_3E" )


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, через этого боты можно купить немного интересного, хочешь узнать цены?")
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Да", callback_data="yes_01")
    callback_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no_01")
    keyboard.add(callback_button, callback_button2)
    bot.send_message(message.chat.id, " ", reply_markup=keyboard)



# кнопки вызывающие действия
@bot.message_handler(content_types=["text"])
def any_msg(message):
    answer = "Недопустимый вариант ответа"
    bot.send_message(message.chat.id, answer)


#обработчик (кнопки вызывающие действия)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "yes_01":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Решай скорее")
            bot.send_message(chat_id=call.message.chat.id,text="ЗБс щас все будет")
            bot.send_message(chat_id=call.message.chat.id, text= "Пикачу 1 штука =20грн \n"
                                                                 "Умпа лумпы 1 штука =30 грн\n"
                                                                 "Поцеловать админа в жопу = бесценно\n"
                                                                 )
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Да", callback_data="yes_02")
            callback_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no_01")
            keyboard.add(callback_button, callback_button2)
            bot.send_message(chat_id=call.message.chat.id,text="Подходят тебе цены или нет?", reply_markup=keyboard)




        elif call.data == "no_01":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ну и пошел нахуй отсюдова")
        elif call.data == "yes_02":
            keyboard = types.InlineKeyboardMarkup()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Подходят тебе цены или нет?")
            callback_button = types.InlineKeyboardButton(text="Район 1", callback_data="ter_01")
            callback_button2 = types.InlineKeyboardButton(text="Район 2", callback_data="ter_02")
            callback_button3 = types.InlineKeyboardButton(text="Район 3", callback_data="ter_03")
            callback_button4 = types.InlineKeyboardButton(text="Район 4", callback_data="ter_04")
            keyboard.add(callback_button, callback_button2, callback_button3, callback_button4)
            bot.send_message(chat_id=call.message.chat.id, text="Попробуй понять где ты и выбери свой район", reply_markup=keyboard)
        elif call.data == "ter_01":
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Нидоран 2грам", callback_data="ter_01_01")
            callback_button2 = types.InlineKeyboardButton(text="Пиджи 3грам", callback_data="ter_01_02")
            callback_button3 = types.InlineKeyboardButton(text="Оникс 4грам", callback_data="ter_01_03")
            callback_button4 = types.InlineKeyboardButton(text="Ебументов килограмм", callback_data="ter_01_04")
            keyboard.add(callback_button, callback_button2, callback_button3, callback_button4)
            bot.send_message(chat_id=call.message.chat.id, text="Выбери покемона который тебя интересует из этого списка ", reply_markup=keyboard)
        elif call.data == "ter_02":
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Нидоран 2грам", callback_data="ter_02_01")
            callback_button2 = types.InlineKeyboardButton(text="Пиджи 3грам", callback_data="ter_02_02")
            callback_button3 = types.InlineKeyboardButton(text="Оникс 4грам", callback_data="ter_02_03")
            callback_button4 = types.InlineKeyboardButton(text="Ебументов килограмм", callback_data="ter_02_04")
            keyboard.add(callback_button, callback_button2, callback_button3, callback_button4)
            bot.send_message(chat_id=call.message.chat.id, text="Выбери покемона который тебя интересует из этого списка ", reply_markup=keyboard)
        elif call.data == "ter_03":
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Нидоран 2грам", callback_data="ter_03_01")
            callback_button2 = types.InlineKeyboardButton(text="Пиджи 3грам", callback_data="ter_03_02")
            callback_button3 = types.InlineKeyboardButton(text="Оникс 4грам", callback_data="ter_03_03")
            callback_button4 = types.InlineKeyboardButton(text="Ебументов килограмм", callback_data="ter_03_04")
            keyboard.add(callback_button, callback_button2, callback_button3, callback_button4)
            bot.send_message(chat_id=call.message.chat.id, text="Выбери покемона который тебя интересует из этого списка ", reply_markup=keyboard)
        elif call.data == "ter_04":
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Нидоран 2грам", callback_data="ter_04_01")
            callback_button2 = types.InlineKeyboardButton(text="Пиджи 3грам", callback_data="ter_04_02")
            callback_button3 = types.InlineKeyboardButton(text="Оникс 4грам", callback_data="ter_04_03")
            callback_button4 = types.InlineKeyboardButton(text="Ебументов килограмм", callback_data="ter_04_04")
            keyboard.add(callback_button, callback_button2, callback_button3, callback_button4)
            bot.send_message(chat_id=call.message.chat.id, text="Выбери покемона который тебя интересует из этого списка ", reply_markup=keyboard)
        elif call.data == "ter_01_01":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_01_02":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_01_03":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_01_04":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_02_01":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_02_02":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_02_03":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_02_04":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_03_01":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_03_02":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_03_03":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_03_03":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_03_04":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_04_01":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_04_02":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_04_03":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)
        elif call.data == "ter_04_04":
            bot.send_message(chat_id=call.message.chat.id, text="ЗБс щас все будет")
            bot.send_photo(chat_id=call.message.chat.id,photo='https://cdn.bulbagarden.net/upload/4/4a/032Nidoran.png' )
            bot.send_location(chat_id=call.message.chat.id,latitude=50.448702, longitude=30.458782)

bot.polling( none_stop=True )



