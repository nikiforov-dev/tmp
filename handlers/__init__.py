from aiogram import Dispatcher

from handlers.callbacks import register_callbacks
from handlers.commands import register_commands
from handlers.messages import register_messages
from handlers.setup import register_setup


def register_handlers(dp: Dispatcher):
    register_commands(dp)
    register_messages(dp)
    register_callbacks(dp)
    register_setup(dp)
