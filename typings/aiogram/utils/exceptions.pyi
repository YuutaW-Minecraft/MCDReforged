"""
This type stub file was generated by pyright.
"""

"""
- TelegramAPIError
    - ValidationError
    - Throttled
    - BadRequest
        - MessageError
            - MessageNotModified
            - MessageToForwardNotFound
            - MessageToDeleteNotFound
            - MessageToPinNotFound
            - MessageIdentifierNotSpecified
            - MessageTextIsEmpty
            - MessageCantBeEdited
            - MessageCantBeDeleted
            - MessageCantBeForwarded
            - MessageToEditNotFound
            - MessageToReplyNotFound
            - ToMuchMessages
        - PollError
            - PollCantBeStopped
            - PollHasAlreadyClosed
            - PollsCantBeSentToPrivateChats
            - PollSizeError
                - PollMustHaveMoreOptions
                - PollCantHaveMoreOptions
                - PollsOptionsLengthTooLong
                - PollOptionsMustBeNonEmpty
                - PollQuestionMustBeNonEmpty
            - MessageWithPollNotFound (with MessageError)
            - MessageIsNotAPoll (with MessageError)
        - ObjectExpectedAsReplyMarkup
        - InlineKeyboardExpected
        - ChatNotFound
        - ChatDescriptionIsNotModified
        - InvalidQueryID
        - InvalidPeerID
        - InvalidHTTPUrlContent
        - ButtonURLInvalid
        - URLHostIsEmpty
        - StartParamInvalid
        - ButtonDataInvalid
        - FileIsTooBig
        - WrongFileIdentifier
        - GroupDeactivated
        - BadWebhook
            - WebhookRequireHTTPS
            - BadWebhookPort
            - BadWebhookAddrInfo
            - BadWebhookNoAddressAssociatedWithHostname
        - NotFound
            - MethodNotKnown
        - PhotoAsInputFileRequired
        - InvalidStickersSet
        - NoStickerInRequest
        - ChatAdminRequired
        - NeedAdministratorRightsInTheChannel
        - MethodNotAvailableInPrivateChats
        - CantDemoteChatCreator
        - CantRestrictSelf
        - NotEnoughRightsToRestrict
        - PhotoDimensions
        - UnavailableMembers
        - TypeOfFileMismatch
        - WrongRemoteFileIdSpecified
        - PaymentProviderInvalid
        - CurrencyTotalAmountInvalid
        - CantParseUrl
        - UnsupportedUrlProtocol
        - CantParseEntities
        - ResultIdDuplicate
        - MethodIsNotAvailable
    - ConflictError
        - TerminatedByOtherGetUpdates
        - CantGetUpdates
    - Unauthorized
        - BotKicked
        - BotBlocked
        - UserDeactivated
        - CantInitiateConversation
        - CantTalkWithBots
    - NetworkError
    - RetryAfter
    - MigrateToChat
    - RestartingTelegram

- AIOGramWarning
    - TimeoutWarning
"""
_PREFIXES = ['error: ', '[error]: ', 'bad request: ', 'conflict: ', 'not found: ']
class TelegramAPIError(Exception):
    def __init__(self, message=...) -> None:
        ...
    


class _MatchErrorMixin:
    match = ...
    text = ...
    __subclasses = ...
    def __init_subclass__(cls, **kwargs):
        ...
    
    @classmethod
    def check(cls, message) -> bool:
        """
        Compare pattern with message

        :param message: always must be in lowercase
        :return: bool
        """
        ...
    
    @classmethod
    def detect(cls, description):
        ...
    


class AIOGramWarning(Warning):
    ...


class TimeoutWarning(AIOGramWarning):
    ...


class FSMStorageWarning(AIOGramWarning):
    ...


class ValidationError(TelegramAPIError):
    ...


class BadRequest(TelegramAPIError, _MatchErrorMixin):
    __group = ...


class MessageError(BadRequest):
    __group = ...


class MessageNotModified(MessageError):
    """
    Will be raised when you try to set new text is equals to current text.
    """
    match = ...


class MessageToForwardNotFound(MessageError):
    """
    Will be raised when you try to forward very old or deleted or unknown message.
    """
    match = ...


class MessageToDeleteNotFound(MessageError):
    """
    Will be raised when you try to delete very old or deleted or unknown message.
    """
    match = ...


class MessageToPinNotFound(MessageError):
    """
    Will be raised when you try to pin deleted or unknown message.
    """
    match = ...


class MessageToReplyNotFound(MessageError):
    """
    Will be raised when you try to reply to very old or deleted or unknown message.
    """
    match = ...


class MessageIdentifierNotSpecified(MessageError):
    match = ...


class MessageTextIsEmpty(MessageError):
    match = ...


class MessageCantBeEdited(MessageError):
    match = ...


class MessageCantBeDeleted(MessageError):
    match = ...


class MessageCantBeForwarded(MessageError):
    match = ...


class MessageToEditNotFound(MessageError):
    match = ...


class MessageIsTooLong(MessageError):
    match = ...


class ToMuchMessages(MessageError):
    """
    Will be raised when you try to send media group with more than 10 items.
    """
    match = ...


class ObjectExpectedAsReplyMarkup(BadRequest):
    match = ...


class InlineKeyboardExpected(BadRequest):
    match = ...


class PollError(BadRequest):
    __group = ...


class PollCantBeStopped(PollError):
    match = ...


class PollHasAlreadyBeenClosed(PollError):
    match = ...


class PollsCantBeSentToPrivateChats(PollError):
    match = ...


class PollSizeError(PollError):
    __group = ...


class PollMustHaveMoreOptions(PollSizeError):
    match = ...


class PollCantHaveMoreOptions(PollSizeError):
    match = ...


class PollOptionsMustBeNonEmpty(PollSizeError):
    match = ...


class PollQuestionMustBeNonEmpty(PollSizeError):
    match = ...


class PollOptionsLengthTooLong(PollSizeError):
    match = ...


class PollQuestionLengthTooLong(PollSizeError):
    match = ...


class PollCanBeRequestedInPrivateChatsOnly(PollError):
    match = ...


class MessageWithPollNotFound(PollError, MessageError):
    """
    Will be raised when you try to stop poll with message without poll
    """
    match = ...


class MessageIsNotAPoll(PollError, MessageError):
    """
    Will be raised when you try to stop poll with message without poll
    """
    match = ...


class ChatNotFound(BadRequest):
    match = ...


class ChatIdIsEmpty(BadRequest):
    match = ...


class InvalidUserId(BadRequest):
    match = ...
    text = ...


class ChatDescriptionIsNotModified(BadRequest):
    match = ...


class InvalidQueryID(BadRequest):
    match = ...


class InvalidPeerID(BadRequest):
    match = ...
    text = ...


class InvalidHTTPUrlContent(BadRequest):
    match = ...


class ButtonURLInvalid(BadRequest):
    match = ...
    text = ...


class URLHostIsEmpty(BadRequest):
    match = ...


class StartParamInvalid(BadRequest):
    match = ...
    text = ...


class ButtonDataInvalid(BadRequest):
    match = ...
    text = ...


class FileIsTooBig(BadRequest):
    match = ...


class WrongFileIdentifier(BadRequest):
    match = ...


class GroupDeactivated(BadRequest):
    match = ...


class PhotoAsInputFileRequired(BadRequest):
    """
    Will be raised when you try to set chat photo from file ID.
    """
    match = ...


class InvalidStickersSet(BadRequest):
    match = ...
    text = ...


class NoStickerInRequest(BadRequest):
    match = ...


class ChatAdminRequired(BadRequest):
    match = ...
    text = ...


class NeedAdministratorRightsInTheChannel(BadRequest):
    match = ...
    text = ...


class NotEnoughRightsToPinMessage(BadRequest):
    match = ...


class MethodNotAvailableInPrivateChats(BadRequest):
    match = ...


class CantDemoteChatCreator(BadRequest):
    match = ...


class CantRestrictSelf(BadRequest):
    match = ...
    text = ...


class NotEnoughRightsToRestrict(BadRequest):
    match = ...


class PhotoDimensions(BadRequest):
    match = ...
    text = ...


class UnavailableMembers(BadRequest):
    match = ...


class TypeOfFileMismatch(BadRequest):
    match = ...


class WrongRemoteFileIdSpecified(BadRequest):
    match = ...


class PaymentProviderInvalid(BadRequest):
    match = ...
    text = ...


class CurrencyTotalAmountInvalid(BadRequest):
    match = ...
    text = ...


class BadWebhook(BadRequest):
    __group = ...


class WebhookRequireHTTPS(BadWebhook):
    match = ...
    text = ...


class BadWebhookPort(BadWebhook):
    match = ...
    text = ...


class BadWebhookAddrInfo(BadWebhook):
    match = ...
    text = ...


class BadWebhookNoAddressAssociatedWithHostname(BadWebhook):
    match = ...


class CantParseUrl(BadRequest):
    match = ...


class UnsupportedUrlProtocol(BadRequest):
    match = ...


class CantParseEntities(BadRequest):
    match = ...


class ResultIdDuplicate(BadRequest):
    match = ...
    text = ...


class BotDomainInvalid(BadRequest):
    match = ...
    text = ...


class MethodIsNotAvailable(BadRequest):
    match = ...


class NotFound(TelegramAPIError, _MatchErrorMixin):
    __group = ...


class MethodNotKnown(NotFound):
    match = ...


class ConflictError(TelegramAPIError, _MatchErrorMixin):
    __group = ...


class TerminatedByOtherGetUpdates(ConflictError):
    match = ...
    text = ...


class CantGetUpdates(ConflictError):
    match = ...


class Unauthorized(TelegramAPIError, _MatchErrorMixin):
    __group = ...


class BotKicked(Unauthorized):
    match = ...


class BotBlocked(Unauthorized):
    match = ...


class UserDeactivated(Unauthorized):
    match = ...


class CantInitiateConversation(Unauthorized):
    match = ...


class CantTalkWithBots(Unauthorized):
    match = ...


class NetworkError(TelegramAPIError):
    ...


class RestartingTelegram(TelegramAPIError):
    def __init__(self) -> None:
        ...
    


class RetryAfter(TelegramAPIError):
    def __init__(self, retry_after) -> None:
        ...
    


class MigrateToChat(TelegramAPIError):
    def __init__(self, chat_id) -> None:
        ...
    


class Throttled(TelegramAPIError):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


