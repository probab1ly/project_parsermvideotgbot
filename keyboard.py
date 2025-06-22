from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
def takethemodel():
    keyboard = [
        [
            KeyboardButton(text='🍏Apple'),
            KeyboardButton(text='🏅Honor')
        ],
        [
            KeyboardButton(text='🎊Redmi'),
            KeyboardButton(text='✨HUAWEI')
        ],
        [
            KeyboardButton(text='🦾ASUS'),
            KeyboardButton(text='🎮MSI')
        ],
        [
            KeyboardButton(text='💻Thunderobot'),
            KeyboardButton(text='🎱INFINIX')
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def mainkeyboard():
    keyboard = [
        [KeyboardButton(text='✅Activate'), KeyboardButton(text='❌Deactivate')],
        [KeyboardButton(text='Добавить модель'), KeyboardButton(text='Удалить модель')],
        [KeyboardButton(text='Мои модели')]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
