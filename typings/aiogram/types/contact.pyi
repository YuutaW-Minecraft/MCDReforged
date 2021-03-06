"""
This type stub file was generated by pyright.
"""

from . import base

class Contact(base.TelegramObject):
    """
    This object represents a phone contact.

    https://core.telegram.org/bots/api#contact
    """
    phone_number: base.String = ...
    first_name: base.String = ...
    last_name: base.String = ...
    user_id: base.Integer = ...
    vcard: base.String = ...
    @property
    def full_name(self):
        ...
    
    def __hash__(self) -> int:
        ...
    


