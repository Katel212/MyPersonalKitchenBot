from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from app.models import User, ShoppingList, UserSettings
from app.models import Chat


class ACLMiddleware(BaseMiddleware):
    @staticmethod
    async def setup_chat(data: dict, user: types.User, chat: Optional[types.Chat] = None):
        user_id = user.id
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        language = user.language_code
        chat_id = chat.id if chat else user.id
        chat_type = chat.type if chat else "private"

        user: User = await User.get(user_id)
        if user is None:
            user = await User.create(id=user_id,
                                     first_name=first_name,
                                     last_name=last_name,
                                     username=username,
                                     language=language)
            await ShoppingList.create(
                user_id=user.id
            )
            await UserSettings.create(user_id=user.id,
                                      tifications_general_enabled=False,
                                      notifications_advance_enabled=False,
                                      notifications_advance_days_until_expiration=None,
                                      notifications_periodical_frequency=None,
                                      notifications_weekly_enabled=False,
                                      notifications_weekly_day=None)
        chat = await Chat.get(chat_id)
        if chat is None:
            chat = await Chat.create(id=chat_id, type=chat_type)

        data["user"] = user
        data["chat"] = chat

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message.chat)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user, query.message.chat if query.message else None)

