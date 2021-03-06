"""
This type stub file was generated by pyright.
"""

from typing import Type, TypeVar

class DataMixin:
    @property
    def data(self):
        ...
    
    def __getitem__(self, item):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __contains__(self, key):
        ...
    
    def get(self, key, default=...):
        ...
    


T = TypeVar('T')
class ContextInstanceMixin:
    def __init_subclass__(cls, **kwargs):
        ...
    
    @classmethod
    def get_current(cls: Type[T], no_error=...) -> T:
        ...
    
    @classmethod
    def set_current(cls: Type[T], value: T):
        ...
    


