"""
This type stub file was generated by pyright.
"""

from aiohttp import web
from . import base

class AuthWidgetData(base.TelegramObject):
    id: base.Integer = ...
    first_name: base.String = ...
    last_name: base.String = ...
    username: base.String = ...
    photo_url: base.String = ...
    auth_date: base.String = ...
    hash: base.String = ...
    @classmethod
    def parse(cls, request: web.Request) -> AuthWidgetData:
        """
        Parse request as Telegram auth widget data.

        :param request:
        :return: :obj:`AuthWidgetData`
        :raise: :obj:`aiohttp.web.HTTPBadRequest`
        """
        ...
    
    def validate(self):
        ...
    
    @property
    def full_name(self):
        ...
    
    def __hash__(self) -> int:
        ...
    


