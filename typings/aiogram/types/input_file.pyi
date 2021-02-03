"""
This type stub file was generated by pyright.
"""

import io
import logging
from pathlib import Path
from typing import Union
from . import base

CHUNK_SIZE = 65536
log = logging.getLogger('aiogram')
class InputFile(base.TelegramObject):
    """
    This object represents the contents of a file to be uploaded.
    Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.

    Also that is not typical TelegramObject!

    https://core.telegram.org/bots/api#inputfile
    """
    def __init__(self, path_or_bytesio: Union[str, io.IOBase, Path], filename=..., conf=...) -> None:
        """

        :param path_or_bytesio:
        :param filename:
        :param conf:
        """
        ...
    
    def __del__(self):
        """
        Close file descriptor
        """
        ...
    
    @property
    def filename(self):
        ...
    
    @filename.setter
    def filename(self, value):
        ...
    
    @property
    def attach(self):
        ...
    
    def get_filename(self) -> str:
        """
        Get file name

        :return: name
        """
        ...
    
    @property
    def file(self):
        ...
    
    def get_file(self):
        """
        Get file object

        :return:
        """
        ...
    
    @classmethod
    def from_url(cls, url, filename=..., chunk_size=...):
        """
        Download file from URL

        Manually is not required action. You can send urls instead!

        :param url: target URL
        :param filename: optional. set custom file name
        :param chunk_size:

        :return: InputFile
        """
        ...
    
    def save(self, filename, chunk_size=...):
        """
        Write file to disk

        :param filename:
        :param chunk_size:
        """
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def to_python(self):
        ...
    
    @classmethod
    def to_object(cls, data):
        ...
    


class _WebPipe:
    def __init__(self, url, chunk_size=...) -> None:
        ...
    
    @property
    def name(self):
        ...
    
    async def open(self):
        ...
    
    async def close(self):
        ...
    
    @property
    def closed(self):
        ...
    
    def __aiter__(self):
        ...
    
    async def __anext__(self):
        ...
    
    async def read(self, chunk_size=...):
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...


