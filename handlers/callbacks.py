from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery

from keyboards.callback_data import ChannelCallback, VideoCallback, VideoPaginationCallback
from keyboards.inline import create_videos_keyboard, create_channels_keyboard


async def handler_channel_callback(query: CallbackQuery, callback_data: ChannelCallback):
    channel_id: str = callback_data.channel_id

    keyboard = create_videos_keyboard(channel_id)
    await query.message.answer(f"Видео для канала {channel}:", reply_markup=keyboard)


async def handle_video_callback(call: CallbackQuery, callback_data: VideoCallback):
    title = callback_data.title
    await call.message.answer(f"Вы выбрали видео '{title}'")


async def handle_channel_pagination_callback(call: CallbackQuery, callback_data: VideoPaginationCallback):
    channel = callback_data.channel
    keyboard = create_channels_keyboard(channel)

    await call.message.edit_reply_markup(reply_markup=keyboard)


async def handle_video_pagination_callback(call: CallbackQuery, callback_data: VideoPaginationCallback):
    channel = callback_data.channel
    page = callback_data.page
    channel_videos = [video for video in videos if video['channel'] == channel]
    keyboard = create_videos_keyboard(channel_videos, channel)

    await call.message.edit_reply_markup(reply_markup=keyboard)


def register_callbacks(dp: Dispatcher):
    dp.callback_query.register(handler_channel_callback, ChannelCallback.filter())
    dp.callback_query.register(handle_video_callback, VideoCallback.filter())
    dp.callback_query.register(handle_channel_pagination_callback, VideoPaginationCallback.filter())
    dp.callback_query.register(handle_video_pagination_callback, VideoPaginationCallback.filter())
