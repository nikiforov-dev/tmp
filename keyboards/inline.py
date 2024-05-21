from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import PAGE_SIZE, FORWARDS, BACKWARDS, PAGE
from keyboards.callback_data import ChannelCallback, VideoCallback, VideoPaginationCallback, ChannelPaginationCallback

videos = [
    {"id": 1, "channel_id": 1, "title": "Video title", "videos_count": 100500, "description": "Video description"}
]

def create_channels_keyboard(channels, page: int = PAGE, page_size=PAGE_SIZE):
    builder = InlineKeyboardBuilder()

    start: int = page * page_size
    end: int = start + page_size

    for channel in channels[start:end]:
        builder.button(
            text=channel['title'],
            callback_data=ChannelCallback(title=channel['title'], id=channel['id'])
        )

    if start > 0:
        builder.button(
            text=BACKWARDS,
            callback_data=ChannelPaginationCallback(page=page - 1)
        )

    if end <= len(channels):
        builder.button(
            text=FORWARDS,
            callback_data=ChannelPaginationCallback(page=page + 1)
        )
    remaining = len(channels) % page_size
    total_pages = (len(channels) // page_size) if remaining == 0 else (len(channels) // page_size) + 1

    builder.button(
        text=f'{page + 1}/{total_pages}',
        callback_data="noop"
    )

    builder.adjust(1, 1)

    return builder.as_markup()


def create_videos_keyboard(channel_id, page=PAGE, page_size=PAGE_SIZE) -> InlineKeyboardMarkup:
    channel_videos = [video for video in videos if video['channel_id'] == channel_id]

    builder = InlineKeyboardBuilder()

    start: int = page * page_size
    end: int = start + page_size

    for video in channel_videos[start:end]:
        builder.button(
            text=video['title'],
            callback_data=VideoCallback(title=video['title'])
        )

    if start > 0:
        builder.button(
            text=BACKWARDS,
            callback_data=VideoPaginationCallback(page=page - 1)
        )

    if end <= len(channel_videos):
        builder.button(
            text=FORWARDS,
            callback_data=VideoPaginationCallback(page=page + 1, channel_id=)
        )
    remaining = len(channel_videos) % page_size
    total_pages = (len(channel_videos) // page_size) if remaining == 0 else (len(channel_videos) // page_size) + 1

    builder.button(
        text=f'{page + 1}/{total_pages}',
        callback_data="noop"
    )

    builder.adjust(1, 1)

    return builder.as_markup()
