"""
This type stub file was generated by pyright.
"""

import sys
import asyncio
import os
from . import bot, contrib, dispatcher, types, utils
from .bot import Bot
from .dispatcher import Dispatcher, filters, middlewares
from .utils import exceptions, executor, helper, markdown as md

if sys.version_info < (3, 7):
    ...
__version__ = '2.11.2'
__api_version__ = '5.0'