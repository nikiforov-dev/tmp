from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram import html, Dispatcher

from keyboards.inline import create_channels_keyboard
from states import Form

channels = [
        {"id": 1, "title": "Channel 1"},
        {"id": 2, "title": "Channel 2"},
        {"id": 3, "title": "Channel 2"},
        {"id": 4, "title": "Channel 2"},
        {"id": 5, "title": "Channel 2"},
        {"id": 6, "title": "Channel 2"},
        {"id": 7, "title": "Channel 2"},
        {"id": 8, "title": "Channel 2"},
        {"id": 9, "title": "Channel 2"},
        {"id": 10, "title": "Channel 2"},
        {"id": 11, "title": "Channel 2"},
        {"id": 12, "title": "Channel 2"},
        {"id": 13, "title": "Channel 2"},
        {"id": 14, "title": "Channel 2"},
        {"id": 15, "title": "Channel 2"},
    ]


async def start(message: Message):
    await message.answer(f'Привет, {html.bold(message.from_user.full_name)}!\n'
                         f'В прошлой жизни я был кровавым диктатором, развязывал войны и ел людей. '
                         'Поэтому сейчас я помогу тебе спарсить канал на Rutube!')


async def parse_channel(message: Message, state: FSMContext):
    await message.answer('Пришлите ссылку на канал, который нужно спарсить.')
    await state.set_state(Form.waiting_for_link)


async def show_channels(message: Message):
    await message.answer(f'Каналы, которые вы парсили.', reply_markup=create_channels_keyboard(channels))


def register_commands(dp: Dispatcher):
    dp.message.register(start, CommandStart())
    dp.message.register(parse_channel, Command('parse_channel'))
    dp.message.register(show_channels, Command('show_channels'))

