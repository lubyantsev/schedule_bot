from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_days_keyboard(selected_times=None, user_name=None):
    days_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [
        ['ПН 401 18:00', 'ПН 401 19:00'],
        ['ПН 401 20:00', 'ПН 401 21:00'],
        ['СР 401 18:00', 'СР 401 19:00'],
        ['СР 401 20:00', 'СР 401 21:00'],
        ['ЧТ 416 20:00', 'ЧТ 416 21:00'],
        ['СБ 416 17:00', 'СБ 416 18:00'],
        ['СБ 416 19:00', 'СБ 416 20:00'],
        ['СБ 416 21:00', 'ВС 415 11:00'],
        ['ВС 415 12:00', 'Завершить выбор']
    ]

    for row in buttons:
        days_keyboard.row(*(KeyboardButton(btn) for btn in row))

    if selected_times and user_name:
        for time in selected_times:
            for i, row in enumerate(buttons):
                for j, btn in enumerate(row):
                    if btn == time:
                        buttons[i][j] = f"{btn} ({user_name})"

    days_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for row in buttons:
        days_keyboard.row(*(KeyboardButton(btn) for btn in row))

    return days_keyboard
