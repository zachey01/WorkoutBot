import telebot
import config
import workout_data

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id, 
                     config.START_MESSAGE,
                     parse_mode='html',
                     reply_markup=default_keyboard(message.chat.id))


@bot.message_handler(content_types=['text'])
def on_message_received(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        msg_text = message.text  # .encode('utf-8')
        if msg_text == config.BUTTON_ADDITIONALLY_1:
            msg = "<b><u>За все время:</u></b> \n\n"
            for key in ["Пресс", "Брусья", "Отжимания", "Подтягивания"]:
                msg = msg + "" + key + ": " + str(workout_data.get_sum_for_key(chat_id, key)) + " раз\n"
            bot.send_message(chat_id, msg, parse_mode='html')
        elif msg_text == config.BUTTON_ADDITIONALLY_2:
            json_data = workout_data.get_workout_data_json(chat_id)
            msg = "<b><u>Подробная статистика:</u></b> \n\n"
            for key in json_data.keys():
                msg += "<u>" + key + "</u> \n"
                for key2 in ["Пресс", "Брусья", "Отжимания", "Подтягивания"]:
                    msg += "" + key2 + ": " + str(workout_data.get_date_for_key(chat_id, key, key2)) + " раз\n"
                msg += "\n"
            bot.send_message(chat_id, msg, parse_mode='html')
        elif msg_text == config.BUTTON_CANCEL:
            bot.send_message(chat_id, msg_text, reply_markup=default_keyboard(chat_id))
        elif msg_text == config.BUTTON_SELECTOR_1 or msg_text == config.BUTTON_SELECTOR_2 or msg_text == config.BUTTON_SELECTOR_3 or msg_text == config.BUTTON_SELECTOR_4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in range(1, 6):
                btn = types.KeyboardButton(str(10 + i * 5) + " " + msg_text)
                markup.add(btn)
            markup.add(config.BUTTON_CANCEL)
            bot.send_message(chat_id, msg_text, reply_markup=markup)
        elif msg_text[:2].isdigit():
            key = msg_text[3:]
            value = int(msg_text[:2])
            workout_data.update_json_data(chat_id, key, value)
            msg = "<b><u>Сегодня:</u></b> \n\n"
            for key in ["Пресс", "Брусья", "Отжимания", "Подтягивания"]:
                msg = msg + "" + key + ": " + str(workout_data.get_today_for_key(chat_id, key)) + " раз\n"
            bot.send_message(chat_id, msg, reply_markup=default_keyboard(chat_id), parse_mode='html')
        else:
            bot.send_message(chat_id, "Я тебя не понимаю", reply_markup=default_keyboard(chat_id))


def default_keyboard(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton(config.BUTTON_SELECTOR_1)
    btn2 = types.KeyboardButton(config.BUTTON_SELECTOR_2)
    btn3 = types.KeyboardButton(config.BUTTON_SELECTOR_3)
    btn4 = types.KeyboardButton(config.BUTTON_SELECTOR_4)
    btn5 = types.KeyboardButton(config.BUTTON_ADDITIONALLY_1)
    btn6 = types.KeyboardButton(config.BUTTON_ADDITIONALLY_2)

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    markup.add(btn6)

    return markup


print("Бот успешно запущен!")
bot.polling(none_stop=True)