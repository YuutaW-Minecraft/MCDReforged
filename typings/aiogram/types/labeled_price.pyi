"""
This type stub file was generated by pyright.
"""

from . import base

class LabeledPrice(base.TelegramObject):
    """
    This object represents a portion of the price for goods or services.

    https://core.telegram.org/bots/api#labeledprice
    """
    label: base.String = ...
    amount: base.Integer = ...
    def __init__(self, label: base.String, amount: base.Integer) -> None:
        ...
    


