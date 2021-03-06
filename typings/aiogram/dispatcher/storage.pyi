"""
This type stub file was generated by pyright.
"""

import typing

KEY = 'key'
LAST_CALL = 'called_at'
RATE_LIMIT = 'rate_limit'
RESULT = 'result'
EXCEEDED_COUNT = 'exceeded'
DELTA = 'delta'
THROTTLE_MANAGER = '$throttle_manager'
class BaseStorage:
    """
    You are able to save current user's state
    and data for all steps in states-storage
    """
    async def close(self):
        """
        You have to override this method and use when application shutdowns.
        Perhaps you would like to save data and etc.

        :return:
        """
        ...
    
    async def wait_closed(self):
        """
        You have to override this method for all asynchronous storages (e.g., Redis).

        :return:
        """
        ...
    
    @classmethod
    def check_address(cls, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ...) -> (typing.Union[str, int], typing.Union[str, int]):
        """
        In all storage's methods chat or user is always required.
        If one of them is not provided, you have to set missing value based on the provided one.

        This method performs the check described above.

        :param chat:
        :param user:
        :return:
        """
        ...
    
    async def get_state(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., default: typing.Optional[str] = ...) -> typing.Optional[str]:
        """
        Get current state of user in chat. Return `default` if no record is found.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :param default:
        :return:
        """
        ...
    
    async def get_data(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., default: typing.Optional[typing.Dict] = ...) -> typing.Dict:
        """
        Get state-data for user in chat. Return `default` if no data is provided in storage.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :param default:
        :return:
        """
        ...
    
    async def set_state(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., state: typing.Optional[typing.AnyStr] = ...):
        """
        Set new state for user in chat

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :param state:
        """
        ...
    
    async def set_data(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., data: typing.Dict = ...):
        """
        Set data for user in chat

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :param data:
        """
        ...
    
    async def update_data(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., data: typing.Dict = ..., **kwargs):
        """
        Update data for user in chat

        You can use data parameter or|and kwargs.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param data:
        :param chat:
        :param user:
        :param kwargs:
        :return:
        """
        ...
    
    async def reset_data(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ...):
        """
        Reset data for user in chat.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :return:
        """
        ...
    
    async def reset_state(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., with_data: typing.Optional[bool] = ...):
        """
        Reset state for user in chat.
        You may desire to use this method when finishing conversations.

        Chat or user is always required. If one of this is not presented,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :param with_data:
        :return:
        """
        ...
    
    async def finish(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ...):
        """
        Finish conversation for user in chat.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :return:
        """
        ...
    
    def has_bucket(self):
        ...
    
    async def get_bucket(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., default: typing.Optional[dict] = ...) -> typing.Dict:
        """
        Get bucket for user in chat. Return `default` if no data is provided in storage.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :param default:
        :return:
        """
        ...
    
    async def set_bucket(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., bucket: typing.Dict = ...):
        """
        Set bucket for user in chat

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :param bucket:
        """
        ...
    
    async def update_bucket(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., bucket: typing.Dict = ..., **kwargs):
        """
        Update bucket for user in chat

        You can use bucket parameter or|and kwargs.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param bucket:
        :param chat:
        :param user:
        :param kwargs:
        :return:
        """
        ...
    
    async def reset_bucket(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ...):
        """
        Reset bucket dor user in chat.

        Chat or user is always required. If one of them is not provided,
        you have to set missing value based on the provided one.

        :param chat:
        :param user:
        :return:
        """
        ...
    


class FSMContext:
    def __init__(self, storage, chat, user) -> None:
        ...
    
    def proxy(self):
        ...
    
    async def get_state(self, default: typing.Optional[str] = ...) -> typing.Optional[str]:
        ...
    
    async def get_data(self, default: typing.Optional[str] = ...) -> typing.Dict:
        ...
    
    async def update_data(self, data: typing.Dict = ..., **kwargs):
        ...
    
    async def set_state(self, state: typing.Optional[typing.AnyStr] = ...):
        ...
    
    async def set_data(self, data: typing.Dict = ...):
        ...
    
    async def reset_state(self, with_data: typing.Optional[bool] = ...):
        ...
    
    async def reset_data(self):
        ...
    
    async def finish(self):
        ...
    


class FSMContextProxy:
    def __init__(self, fsm_context: FSMContext) -> None:
        ...
    
    async def __aenter__(self):
        ...
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        ...
    
    @classmethod
    async def create(cls, fsm_context: FSMContext):
        """
        :param fsm_context:
        :return:
        """
        ...
    
    async def load(self):
        ...
    
    @property
    def state(self):
        ...
    
    @state.setter
    def state(self, value):
        ...
    
    @state.deleter
    def state(self):
        ...
    
    async def save(self, force=...):
        ...
    
    def clear(self):
        ...
    
    def get(self, value, default=...):
        ...
    
    def setdefault(self, key, default):
        ...
    
    def update(self, data=..., **kwargs):
        ...
    
    def pop(self, key, default=...):
        ...
    
    def keys(self):
        ...
    
    def values(self):
        ...
    
    def items(self):
        ...
    
    def as_dict(self):
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, item):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __contains__(self, item):
        ...
    
    def __str__(self) -> str:
        ...
    


class DisabledStorage(BaseStorage):
    """
    Empty storage. Use it if you don't want to use Finite-State Machine
    """
    async def close(self):
        ...
    
    async def wait_closed(self):
        ...
    
    async def get_state(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., default: typing.Optional[str] = ...) -> typing.Optional[str]:
        ...
    
    async def get_data(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., default: typing.Optional[str] = ...) -> typing.Dict:
        ...
    
    async def update_data(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., data: typing.Dict = ..., **kwargs):
        ...
    
    async def set_state(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., state: typing.Optional[typing.AnyStr] = ...):
        ...
    
    async def set_data(self, *, chat: typing.Union[str, int, None] = ..., user: typing.Union[str, int, None] = ..., data: typing.Dict = ...):
        ...
    


