from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from parsing import (
    parse, products_finally, main_checkpricesandnotify,
    activateadd, deactivateremove, get_active_users, periodcheck, add_model_for_user,
    remove_model_for_user, get_models_for_user)
from keyboard import takethemodel, mainkeyboard
import asyncio
chat_id = 1653541807
# prices_file = 'parser.csv'
# users_file = 'activate_users.txt'
router = Router()

@router.message(Command('start'))
async def start_main(message: Message):
    await message.answer('👋 Привет! Добро пожаловать в наш бот! \n' 
                         'О какой модели ноутбука ты хочешь первым получать информацию?🚀',
                          reply_markup=mainkeyboard())

@router.message(F.text == '✅Activate')
async def activatefunc(message: Message):
    await activateadd(message.from_user.id)
    await message.answer('✅ Уведомления активированы!\nТеперь вы будете получать оповещения о смене цен')

@router.message(F.text == '❌Deactivate')
async def deactivatefunc(message: Message):
    await deactivateremove(message.from_user.id)
    await message.answer('❌ Уведомления отключены.\nВы не будете получать оповещения.')

@router.message(F.text == 'Добавить модель')
async def add_model_button(message: Message):
    await message.answer('Выберите модель для добавления:', reply_markup=takethemodel())

@router.message(F.text == 'Удалить модель')
async def remove_model_button(message: Message):
    await message.answer('Выберите модель для удаления:', reply_markup=takethemodel())

@router.message(F.text.in_(['🍏Apple','🏅Honor','🎊Redmi','✨HUAWEI','🦾ASUS','🎮MSI','💻Thunderobot','🎱INFINIX']))
async def model_choice(message: Message):
    model_map = {
        '🍏Apple': 'Apple',
        '🏅Honor': 'Honor',
        '🎊Redmi': 'Redmi',
        '✨HUAWEI': 'HUAWEI',
        '🦾ASUS': 'ASUS',
        '🎮MSI': 'MSI',
        '💻Thunderobot': 'Thunderobot',
        '🎱INFINIX': 'INFINIX',
    }
    model_name = model_map.get(message.text)
    user_models = get_models_for_user(message.from_user.id)
    if model_name in user_models:
        remove_model_for_user(message.from_user.id, model_name)
        await message.answer(f'Модель "{model_name}" удалена из вашего списка отслеживания.', reply_markup=mainkeyboard())
    else:
        add_model_for_user(message.from_user.id, model_name)
        await message.answer(f'Модель "{model_name}" добавлена в ваш список отслеживания!', reply_markup=mainkeyboard())

@router.message(F.text == 'Мои модели')
async def get_my_models(message: Message):
    models = get_models_for_user(message.from_user.id)
    if not models:
        await message.answer('У вас нет выбранных моделей. Добавьте их кнопкой "Добавить модель".')
    else:
        await message.answer('Ваши выбранные модели:\n' + '\n'.join(models))


