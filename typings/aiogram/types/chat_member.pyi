"""
This type stub file was generated by pyright.
"""

import datetime
from . import base
from .user import User
from ..utils import helper

class ChatMember(base.TelegramObject):
    """
    This object contains information about one member of a chat.

    https://core.telegram.org/bots/api#chatmember
    """
    user: User = ...
    status: base.String = ...
    custom_title: base.String = ...
    is_anonymous: base.Boolean = ...
    until_date: datetime.datetime = ...
    can_be_edited: base.Boolean = ...
    can_change_info: base.Boolean = ...
    can_post_messages: base.Boolean = ...
    can_edit_messages: base.Boolean = ...
    can_delete_messages: base.Boolean = ...
    can_invite_users: base.Boolean = ...
    can_restrict_members: base.Boolean = ...
    can_pin_messages: base.Boolean = ...
    can_promote_members: base.Boolean = ...
    is_member: base.Boolean = ...
    can_send_messages: base.Boolean = ...
    can_send_media_messages: base.Boolean = ...
    can_send_polls: base.Boolean = ...
    can_send_other_messages: base.Boolean = ...
    can_add_web_page_previews: base.Boolean = ...
    def is_chat_creator(self) -> bool:
        ...
    
    def is_chat_admin(self) -> bool:
        ...
    
    def is_chat_member(self) -> bool:
        ...
    
    def __int__(self) -> int:
        ...
    


class ChatMemberStatus(helper.Helper):
    """
    Chat member status
    """
    mode = ...
    CREATOR = ...
    ADMINISTRATOR = ...
    MEMBER = ...
    RESTRICTED = ...
    LEFT = ...
    KICKED = ...
    @classmethod
    def is_chat_creator(cls, role: str) -> bool:
        ...
    
    @classmethod
    def is_chat_admin(cls, role: str) -> bool:
        ...
    
    @classmethod
    def is_chat_member(cls, role: str) -> bool:
        ...
    


