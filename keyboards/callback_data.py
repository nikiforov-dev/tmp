from aiogram.filters.callback_data import CallbackData


class ChannelCallback(CallbackData, prefix="channel"):
    id: int
    title: str


class VideoCallback(CallbackData, prefix='video'):
    id: int
    title: str


class VideoPaginationCallback(CallbackData, prefix='video_pagination'):
    page: int
    channel_id: int


class ChannelPaginationCallback(CallbackData, prefix='channel_pagination'):
    page: int
