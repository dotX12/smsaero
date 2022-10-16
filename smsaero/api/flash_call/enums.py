from enum import Enum


class FlashCallStatus(int, Enum):
    IN_QUEUE = 0
    SUCCESS = 1
    ERROR = 2
    TRANSFER_TO_OPERATOR = 4


class FlashCallURL(str, Enum):
    SEND = "v2/flashcall/send"  # NOQA
    GET_ONE = "v2/flashcall/status"  # NOQA
    GET_ALL = "v2/flashcall/list"  # NOQA
