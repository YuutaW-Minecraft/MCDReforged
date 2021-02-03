"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import Any, Callable, Optional, Union
from aiohttp import web
from aiohttp.web_app import Application
from ..dispatcher.dispatcher import Dispatcher

APP_EXECUTOR_KEY = 'APP_EXECUTOR'
def start_polling(dispatcher, *, loop=..., skip_updates=..., reset_webhook=..., on_startup=..., on_shutdown=..., timeout=..., relax=..., fast=...):
    """
    Start bot in long-polling mode

    :param dispatcher:
    :param loop:
    :param skip_updates:
    :param reset_webhook:
    :param on_startup:
    :param on_shutdown:
    :param timeout:
    """
    ...

def set_webhook(dispatcher: Dispatcher, webhook_path: str, *, loop: Optional[asyncio.AbstractEventLoop] = ..., skip_updates: bool = ..., on_startup: Optional[Callable] = ..., on_shutdown: Optional[Callable] = ..., check_ip: bool = ..., retry_after: Optional[Union[str, int]] = ..., route_name: str = ..., web_app: Optional[Application] = ...):
    """
    Set webhook for bot

    :param dispatcher: Dispatcher
    :param webhook_path: str
    :param loop: Optional[asyncio.AbstractEventLoop] (default: None)
    :param skip_updates: bool (default: None)
    :param on_startup: Optional[Callable] (default: None)
    :param on_shutdown: Optional[Callable] (default: None)
    :param check_ip: bool (default: False)
    :param retry_after: Optional[Union[str, int]] See https://tools.ietf.org/html/rfc7231#section-7.1.3 (default: None)
    :param route_name: str (default: 'webhook_handler')
    :param web_app: Optional[Application] (default: None)
    :return:
    """
    ...

def start_webhook(dispatcher, webhook_path, *, loop=..., skip_updates=..., on_startup=..., on_shutdown=..., check_ip=..., retry_after=..., route_name=..., **kwargs):
    """
    Start bot in webhook mode

    :param dispatcher:
    :param webhook_path:
    :param loop:
    :param skip_updates:
    :param on_startup:
    :param on_shutdown:
    :param check_ip:
    :param route_name:
    :param kwargs:
    :return:
    """
    ...

def start(dispatcher, future, *, loop=..., skip_updates=..., on_startup=..., on_shutdown=...):
    """
    Execute Future.

    :param dispatcher: instance of Dispatcher
    :param future: future
    :param loop: instance of AbstractEventLoop
    :param skip_updates:
    :param on_startup:
    :param on_shutdown:
    :return:
    """
    ...

class Executor:
    """
    Main executor class
    """
    def __init__(self, dispatcher, skip_updates=..., check_ip=..., retry_after=..., loop=...) -> None:
        ...
    
    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        ...
    
    @property
    def frozen(self):
        ...
    
    def set_web_app(self, application: web.Application):
        """
        Change instance of aiohttp.web.Applicaton

        :param application:
        """
        ...
    
    @property
    def web_app(self) -> web.Application:
        ...
    
    def on_startup(self, callback: callable, polling=..., webhook=...):
        """
        Register a callback for the startup process

        :param callback:
        :param polling: use with polling
        :param webhook: use with webhook
        """
        ...
    
    def on_shutdown(self, callback: callable, polling=..., webhook=...):
        """
        Register a callback for the shutdown process

        :param callback:
        :param polling: use with polling
        :param webhook: use with webhook
        """
        ...
    
    def set_webhook(self, webhook_path: Optional[str] = ..., request_handler: Any = ..., route_name: str = ..., web_app: Optional[Application] = ...):
        """
        Set webhook for bot

        :param webhook_path: Optional[str] (default: None)
        :param request_handler: Any (default: WebhookRequestHandler)
        :param route_name: str Name of webhook handler route (default: 'webhook_handler')
        :param web_app: Optional[Application] (default: None)
        :return:
        """
        ...
    
    def run_app(self, **kwargs):
        ...
    
    def start_webhook(self, webhook_path=..., request_handler=..., route_name=..., **kwargs):
        """
        Start bot in webhook mode

        :param webhook_path:
        :param request_handler:
        :param route_name: Name of webhook handler route
        :param kwargs:
        :return:
        """
        ...
    
    def start_polling(self, reset_webhook=..., timeout=..., relax=..., fast=...):
        """
        Start bot in long-polling mode

        :param reset_webhook:
        :param timeout:
        """
        ...
    
    def start(self, future):
        """
        Execute Future.

        Return the Future's result, or raise its exception.

        :param future:
        :return:
        """
        ...
    


