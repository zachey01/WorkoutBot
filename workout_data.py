# -*- coding: utf-8 -*-
import json
import config

from datetime import datetime


def get_workout_data_json():
    return json.load(open(config.JSON_PATH, 'r'))


def get_sum_for_key(key):
    my_sum = 0
    json_data = get_workout_data_json()
    for day_key in json_data.keys():
        day_data = json_data[day_key]
        array = day_data[key]
        for value in array:
            my_sum += value
    return my_sum


def get_today_for_key(key):
    my_sum = 0
    json_data = get_workout_data_json()
    current_day = datetime.now().strftime('%d.%m.%Y')
    day_data = json_data[current_day]
    array = day_data[key]
    for value in array:
        my_sum += value
    return my_sum


def get_date_for_key(date, key):
    my_sum = 0
    json_data = get_workout_data_json()
    day_data = json_data[date]
    array = day_data[key]
    for value in array:
        my_sum += value
    return my_sum


def update_json_data(key, value):
    init_new_day_if_needed()
    json_data = get_workout_data_json()
    current_day = datetime.now().strftime('%d.%m.%Y')
    json_data[current_day][key].append(value)
    open(config.JSON_PATH, 'w').write(json.dumps(json_data, ensure_ascii=False))


# Добавляет сегодняшний день в список (Если его еще не существует)
def init_new_day_if_needed():
    current_day = datetime.now().strftime('%d.%m.%Y')
    json_data = get_workout_data_json()
    if current_day not in json_data:
        json_data[current_day] = config.INIT_JSON_OBJECT
        open(config.JSON_PATH, 'w').write(json.dumps(json_data, ensure_ascii=False))
