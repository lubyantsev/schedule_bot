from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from states import UserState
from keyboards import create_days_keyboard


async def start_command(message: types.Message):
    await UserState.waiting_for_day.set()
    await message.answer("Выберите день и время:", reply_markup=create_days_keyboard())


async def choose_day(message: types.Message, state: FSMContext):
    selected_time = message.text

    if selected_time == 'Завершить выбор':
        await UserState.waiting_for_name.set()
        await message.answer("Введите ваше имя:")
        return

    user_data = await state.get_data()
    selected_times = user_data.get('selected_times', [])
    selected_times.append(selected_time)
    await state.update_data(selected_times=selected_times)

    await message.answer(f"Вы выбрали время: {selected_time}. Выберите еще или завершите выбор.",
                         reply_markup=create_days_keyboard(selected_times))


async def get_name(message: types.Message, state: FSMContext):
    user_name = message.text
    user_data = await state.get_data()
    selected_times = user_data.get('selected_times', [])

    days_keyboard = create_days_keyboard(selected_times, user_name)

    await message.answer(f"Вы выбрали времена: {', '.join(selected_times)}. Нажмите на любую кнопку для подтверждения выбора:",
                         reply_markup=days_keyboard)

    await UserState.waiting_for_confirm.set()


async def confirm_selection(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    selected_times = user_data.get('selected_times', [])
    await message.answer(f"Вы подтвердили выбор времен: {', '.join(selected_times)}")
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(choose_day, state=UserState.waiting_for_day)
    dp.register_message_handler(get_name, state=UserState.waiting_for_name)
    dp.register_message_handler(confirm_selection, state=UserState.waiting_for_confirm)
