"""
This type stub file was generated by pyright.
"""

from . import base
from .callback_query import CallbackQuery
from .chosen_inline_result import ChosenInlineResult
from .inline_query import InlineQuery
from .message import Message
from .poll import Poll, PollAnswer
from .pre_checkout_query import PreCheckoutQuery
from .shipping_query import ShippingQuery
from ..utils import helper

class Update(base.TelegramObject):
    """
    This object represents an incoming update.
    At most one of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api#update
    """
    update_id: base.Integer = ...
    message: Message = ...
    edited_message: Message = ...
    channel_post: Message = ...
    edited_channel_post: Message = ...
    inline_query: InlineQuery = ...
    chosen_inline_result: ChosenInlineResult = ...
    callback_query: CallbackQuery = ...
    shipping_query: ShippingQuery = ...
    pre_checkout_query: PreCheckoutQuery = ...
    poll: Poll = ...
    poll_answer: PollAnswer = ...
    def __hash__(self) -> int:
        ...
    
    def __int__(self) -> int:
        ...
    


class AllowedUpdates(helper.Helper):
    """
    Helper for allowed_updates parameter in getUpdates and setWebhook methods.

    You can use &, + or | operators for make combination of allowed updates.

    Example:
        >>> bot.get_updates(allowed_updates=AllowedUpdates.MESSAGE + AllowedUpdates.EDITED_MESSAGE)
    """
    mode = ...
    MESSAGE = ...
    EDITED_MESSAGE = ...
    CHANNEL_POST = ...
    EDITED_CHANNEL_POST = ...
    INLINE_QUERY = ...
    CHOSEN_INLINE_RESULT = ...
    CALLBACK_QUERY = ...
    SHIPPING_QUERY = ...
    PRE_CHECKOUT_QUERY = ...
    POLL = ...
    POLL_ANSWER = ...
    CHOSEN_INLINE_QUERY = ...


