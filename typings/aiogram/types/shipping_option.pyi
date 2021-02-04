"""
This type stub file was generated by pyright.
"""

import typing
from . import base
from .labeled_price import LabeledPrice

class ShippingOption(base.TelegramObject):
    """
    This object represents one shipping option.

    https://core.telegram.org/bots/api#shippingoption
    """
    id: base.String = ...
    title: base.String = ...
    prices: typing.List[LabeledPrice] = ...
    def __init__(self, id: base.String, title: base.String, prices: typing.List[LabeledPrice] = ...) -> None:
        ...
    
    def add(self, price: LabeledPrice):
        """
        Add price

        :param price:
        :return:
        """
        ...
    

