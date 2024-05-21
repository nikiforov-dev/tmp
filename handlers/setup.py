from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='parse_channel',
            description='Парсинг rutube канала'
        ),
        BotCommand(
            command='show_channels',
            description='Показать мои каналы'
        )

    ]

    await bot.set_my_commands(commands=commands)


def register_setup(dp: Dispatcher):
    dp.startup.register(set_commands)
