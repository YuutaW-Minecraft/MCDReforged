"""
This type stub file was generated by pyright.
"""

from ..utils import helper
from ..utils.deprecated import deprecated
from . import base
from .user import User

class MessageEntity(base.TelegramObject):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity
    """
    type: base.String = ...
    offset: base.Integer = ...
    length: base.Integer = ...
    url: base.String = ...
    user: User = ...
    language: base.String = ...
    def __init__(self, type: base.String, offset: base.Integer, length: base.Integer, url: base.String = ..., user: User = ..., language: base.String = ..., **kwargs) -> None:
        ...
    
    def get_text(self, text):
        """
        Get value of entity

        :param text: full text
        :return: part of text
        """
        ...
    
    @deprecated("This method doesn't work with nested entities and will be removed in aiogram 3.0")
    def parse(self, text, as_html=...):
        """
        Get entity value with markup

        :param text: original text
        :param as_html: as html?
        :return: entity text with markup
        """
        ...
    


class MessageEntityType(helper.Helper):
    """
    List of entity types

    :key: MENTION
    :key: HASHTAG
    :key: CASHTAG
    :key: BOT_COMMAND
    :key: URL
    :key: EMAIL
    :key: PHONE_NUMBER
    :key: BOLD
    :key: ITALIC
    :key: CODE
    :key: PRE
    :key: UNDERLINE
    :key: STRIKETHROUGH
    :key: TEXT_LINK
    :key: TEXT_MENTION
    """
    mode = ...
    MENTION = ...
    HASHTAG = ...
    CASHTAG = ...
    BOT_COMMAND = ...
    URL = ...
    EMAIL = ...
    PHONE_NUMBER = ...
    BOLD = ...
    ITALIC = ...
    CODE = ...
    PRE = ...
    UNDERLINE = ...
    STRIKETHROUGH = ...
    TEXT_LINK = ...
    TEXT_MENTION = ...

