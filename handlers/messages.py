from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import RUTUBE_URL
from states import Form


async def process_link(message: Message, state: FSMContext):
    link: str = message.text
    if not link.startswith(RUTUBE_URL):
        await message.reply('Эта ссылка не с Rutube`a')
        return
    await state.update_data(link=link)
    await message.answer("Спасибо! Теперь укажите количество видео для парсинга.")
    await state.set_state(Form.waiting_for_videos_amount)


async def process_videos_amount(message: Message, state: FSMContext):
    number = message.text
    if number.isdigit():
        num_number = int(number)
    else:
        await message.reply('Это не число!')
        return
    data = await state.get_data()
    link = data.get('link')
    result = f"Ссылка: {link}\nКоличество видео для парсинга: {num_number}"

    await message.answer(f"Спасибо! Сейчас пришлю видео:\n{result}")

    await state.clear()


def register_messages(dp: Dispatcher):
    dp.message.register(Form.waiting_for_link)
    dp.message.register(Form.waiting_for_videos_amount)
