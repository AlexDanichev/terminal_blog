import telebot
from telebot import types
import random
import math

bot = telebot.TeleBot( "845062436:AAGs5eU-tp3_moWfFX3dqFBVGSW14QY6_3E" )

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Йо, братишка! Это чудо техники поможет тебе быстро нарешать приколы.")
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="ГО!", callback_data="yes_01")
    callback_button2 = types.InlineKeyboardButton(text="я не по этим делам", callback_data="no_01")
    keyboard.add(callback_button, callback_button2)
    bot.send_message(message.chat.id, "Заценишь прайс? ", reply_markup=keyboard)


# кнопки вызывающие действия
@bot.message_handler(content_types=["text"])
def any_msg(message):
    answer = "Недопустимый вариант ответа"
    bot.send_message(message.chat.id, answer)
@bot.message_handler(content_types=["photo"])
def pay_photo(message):
    answer = "Скрин отправлен оператору, ожидаю подтверждения"
    bot.send_message(message.chat.id, answer)
    user_name = message.from_user.id
    UsrInfo = bot.get_chat_member(user_name, user_name).user
    f= open("users_shisha_bot.txt", "a+")
    f.write("Id: " + str(UsrInfo.id) + "\nFirst Name: " + str(UsrInfo.first_name) + "\nLast Name: " + str(UsrInfo.last_name) +
                            "\nUsername: @" + str(UsrInfo.username))
    f.close()
#обработчик (кнопки вызывающие действия)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "yes_01":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Заценишь прайс? ")
            bot.send_message(chat_id=call.message.chat.id,text="Щас все будет")
            bot.send_message(chat_id=call.message.chat.id, text= " Шишки\n"
                                                                 "Ак - 47\n"
                                                                 "Сатива, 25 - 27 % ТГК\n"
                                                                 "270 грн - г\n"
                                                                 "450 грн - 2 г\n"
                                                                 "Тополиный пух\n"
                                                                 "70 % сатива / 30 % индика, 25 % ТГК\n"
                                                                 "250 грн - г:\n"
                                                                 "400 грн - 2 г \n"
                                                                 " Белая роза \n"
                                                                 "50 / 50, 23 % ТГК\n"
                                                                 "250  грн - г\n"
                                                                 "400  грн - 2 г\n"
                                                                 ":Jack Hater\n"
                                                                 "50 / 50 25 % ТГК\n"
                                                                 "300 грн - г\n"
                                                                 "500 грн - 2 г\n"
                                                                 "New York\n"
                                                                 "Индика, 22 % ТГК \n"
                                                                 "250 грн - г\n"
                                                                 "400 грн - 2 г\n"
                                                                 " Россыпь \n"
                                                                 " 350 грн - короб\n"
                                                                 "Афганка\n"
                                                                 "500 грн - короб\n"
                                                                 "Амфетамин сульфат 98 %\n"
                                                                 "0.5 - 250 грн\n"
                                                                 "1 г - 400 грн\n"
                                                                 "2 г - 700 грн\n"
                                                                 "Метамфетамин\n"
                                                                 "0.25 - 400 грн\n"
                                                                 "0.5 - 550 грн\n"
                                                                 "1 г - 900 грн\n"
                                                                 )
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Да", callback_data="yes_02")
            callback_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no_01")
            keyboard.add(callback_button, callback_button2)
            bot.send_message(chat_id=call.message.chat.id,text="Хочу намутить", reply_markup=keyboard)




        elif call.data == "no_01":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Всего доброго")
        elif call.data == "yes_03":
            keyboard = types.InlineKeyboardMarkup()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какой вес?")
            callback_button = types.InlineKeyboardButton(text="КПИ-Шулявка", callback_data="ter_01")
            callback_button2 = types.InlineKeyboardButton(text="Нивки", callback_data="ter_02")
            callback_button3 = types.InlineKeyboardButton(text="Центр", callback_data="ter_03")
            callback_button4 = types.InlineKeyboardButton(text="Труханов", callback_data="ter_04")
            keyboard.add(callback_button, callback_button2, callback_button3, callback_button4)
            bot.send_message(chat_id=call.message.chat.id, text="Эй, пират! Выбери райчик где будешь искать клад! Бот скинет примерное гео. "
                                                                "После того, как ты отправишь скрин с оплатой - ")
            bot.send_message(chat_id=call.message.chat.id, text= "- бот пришлет тебе точную локацию стафа", reply_markup=keyboard)
        elif call.data == "yes_02":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хочу намутить")
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Шишки", callback_data="prod_01")
            callback_button2 = types.InlineKeyboardButton(text="Тополиный пух", callback_data="prod_02")
            callback_button3 = types.InlineKeyboardButton(text="Белая роза", callback_data="prod_03")
            callback_button4 = types.InlineKeyboardButton(text="Jack Hater", callback_data="prod_04")
            callback_button5 = types.InlineKeyboardButton(text="New York", callback_data="prod_05")
            callback_button6 = types.InlineKeyboardButton(text="Россыпь", callback_data="prod_06")
            callback_button7 = types.InlineKeyboardButton(text="Афганка", callback_data="prod_07")
            callback_button8 = types.InlineKeyboardButton(text="Амфетамин сульфат 98%", callback_data="prod_08")
            callback_button9 = types.InlineKeyboardButton(text="Метамфетамин", callback_data="prod_09")

            keyboard.add(callback_button, callback_button2, callback_button3, callback_button4,callback_button5,
                         callback_button6,callback_button7,callback_button8,callback_button9)
            bot.send_message(chat_id=call.message.chat.id, text="Теперь выбери товар", reply_markup=keyboard)

        elif call.data == "prod_01":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="1 грамм", callback_data="yes_03")
            callback_button2 = types.InlineKeyboardButton(text="2 грамм", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button, callback_button2,)
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?",reply_markup=keyboard)
        elif call.data == "prod_02":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="1 грамм", callback_data="yes_03")
            callback_button2 = types.InlineKeyboardButton(text="2 грамм", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button, callback_button2, )
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?",reply_markup=keyboard)
        elif call.data == "prod_03":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="1 грамм", callback_data="yes_03")
            callback_button2 = types.InlineKeyboardButton(text="2 грамм", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button, callback_button2, )
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?",reply_markup=keyboard)
        elif call.data == "prod_04":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="1 грамм", callback_data="yes_03")
            callback_button2 = types.InlineKeyboardButton(text="2 грамм", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button, callback_button2, )
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?", reply_markup=keyboard)
        elif call.data == "prod_05":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="1 грамм", callback_data="yes_03")
            callback_button2 = types.InlineKeyboardButton(text="2 грамм", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button, callback_button2, )
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?", reply_markup=keyboard)
        elif call.data == "prod_06":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="КОРОБ", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button )
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?", reply_markup=keyboard)
        elif call.data == "prod_07":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="КОРОБ", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button)
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?", reply_markup=keyboard)
        elif call.data == "prod_08":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="0.5 грамм", callback_data="yes_03")
            callback_button2 = types.InlineKeyboardButton(text="1 грамм", callback_data="yes_03")
            callback_button3 = types.InlineKeyboardButton(text="2 грамм", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button, callback_button2,callback_button3 )
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?",reply_markup=keyboard)
        elif call.data == "prod_09":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Теперь выбери товар")
            callback_button = types.InlineKeyboardButton(text="0.25 грамм", callback_data="yes_03")
            callback_button2 = types.InlineKeyboardButton(text="0.5 грамм", callback_data="yes_03")
            callback_button3 = types.InlineKeyboardButton(text="1 грамм", callback_data="yes_03")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button, callback_button2,callback_button3 )
            bot.send_message(chat_id=call.message.chat.id, text="Какой вес?", reply_markup=keyboard)
        elif call.data == "ter_01":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="- бот пришлет тебе точную локацию стафа")
            bot.send_message(chat_id=call.message.chat.id, text="Жду оплату на карту 1234 4567 1234 5678")
            bot.send_location(chat_id=call.message.chat.id,latitude=random.uniform(50.451161,50.446723),
                              longitude=random.uniform(30.464929,30.443321))
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Подтвердить оплату", callback_data="end")
            keyboard.add(callback_button)
            bot.send_message(chat_id=call.message.chat.id, text="Нажми когда оплатишь", reply_markup=keyboard)
        elif call.data == "ter_02":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="- бот пришлет тебе точную локацию стафа")
            bot.send_message(chat_id=call.message.chat.id, text="Жду оплату на карту 1234 4567 1234 5678")
            bot.send_location(chat_id=call.message.chat.id,latitude=random.uniform(50.466004,50.466190),
                              longitude=random.uniform(30.429729, 30.429774))
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Подтвердить оплату", callback_data="end")
            keyboard.add(callback_button)
            bot.send_message(chat_id=call.message.chat.id, text="Нажми когда оплатишь", reply_markup=keyboard)

        elif call.data == "ter_04":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="- бот пришлет тебе точную локацию стафа")
            bot.send_message(chat_id=call.message.chat.id, text="Жду оплату на карту 1234 4567 1234 5678")
            bot.send_location(chat_id=call.message.chat.id,latitude=random.uniform(50.458203,50.462498),
                              longitude=random.uniform(30.535739, 30.539351))
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Подтвердить оплату", callback_data="end")
            keyboard.add(callback_button)
            bot.send_message(chat_id=call.message.chat.id, text="Нажми когда оплатишь", reply_markup=keyboard)

        elif call.data == "ter_03":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="- бот пришлет тебе точную локацию стафа")
            bot.send_message(chat_id=call.message.chat.id, text="Жду оплату на карту 1234 4567 1234 5678")
            bot.send_location(chat_id=call.message.chat.id,latitude=random.uniform(50.453219,50.442372),
                              longitude=random.uniform(30.520206, 30.498441))
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Подтвердить оплату", callback_data="end")
            keyboard.add(callback_button)
            bot.send_message(chat_id=call.message.chat.id, text="Нажми когда оплатишь", reply_markup=keyboard)

        elif call.data == "end":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Нажми когда оплатишь")
            bot.send_message(chat_id=call.message.chat.id, text="Скинь скриншот")


bot.polling( none_stop=True )



