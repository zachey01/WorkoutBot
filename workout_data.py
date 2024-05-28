import json
import config
import os
from datetime import datetime

def get_workout_data_json(chat_id):
    json_path = config.JSON_PATH + str(chat_id) + ".json"
    if not os.path.exists(json_path):
        # Создаем папку, если её нет
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        # Создаем исходные данные для пользователя
        initial_data = {datetime.now().strftime('%d.%m.%Y'): config.INIT_JSON_OBJECT}
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False)
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_sum_for_key(chat_id, key):
    my_sum = 0
    json_data = get_workout_data_json(chat_id)
    for day_key in json_data.keys():
        day_data = json_data[day_key]
        if key in day_data:
            array = day_data[key]
            for value in array:
                my_sum += value
    return my_sum

def get_today_for_key(chat_id, key):
    my_sum = 0
    json_data = get_workout_data_json(chat_id)
    current_day = datetime.now().strftime('%d.%m.%Y')
    day_data = json_data[current_day]
    array = day_data[key]
    for value in array:
        my_sum += value
    return my_sum

def get_date_for_key(chat_id, date, key):
    my_sum = 0
    json_data = get_workout_data_json(chat_id)
    day_data = json_data[date]
    array = day_data[key]
    for value in array:
        my_sum += value
    return my_sum

def update_json_data(chat_id, key, value):
    init_new_day_if_needed(chat_id)
    json_data = get_workout_data_json(chat_id)
    current_day = datetime.now().strftime('%d.%m.%Y')
    json_data[current_day][key].append(value)
    json_path = config.JSON_PATH + str(chat_id) + ".json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False)

def init_new_day_if_needed(chat_id):
    current_day = datetime.now().strftime('%d.%m.%Y')
    json_path = config.JSON_PATH + str(chat_id) + ".json"
    json_data = get_workout_data_json(chat_id)
    if current_day not in json_data:
        json_data[current_day] = config.INIT_JSON_OBJECT
        with open(json_path, 'w') as f:
            json.dump(json_data, f, ensure_ascii=False)