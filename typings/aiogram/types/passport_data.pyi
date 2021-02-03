"""
This type stub file was generated by pyright.
"""

import typing
from . import base
from .encrypted_credentials import EncryptedCredentials
from .encrypted_passport_element import EncryptedPassportElement

class PassportData(base.TelegramObject):
    """
    Contains information about Telegram Passport data shared with the bot by the user.

    https://core.telegram.org/bots/api#passportdata
    """
    data: typing.List[EncryptedPassportElement] = ...
    credentials: EncryptedCredentials = ...


