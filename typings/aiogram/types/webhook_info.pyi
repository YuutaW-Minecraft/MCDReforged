"""
This type stub file was generated by pyright.
"""

import typing
from . import base

class WebhookInfo(base.TelegramObject):
    """
    Contains information about the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo
    """
    url: base.String = ...
    has_custom_certificate: base.Boolean = ...
    pending_update_count: base.Integer = ...
    ip_address: base.String = ...
    last_error_date: base.Integer = ...
    last_error_message: base.String = ...
    max_connections: base.Integer = ...
    allowed_updates: typing.List[base.String] = ...


