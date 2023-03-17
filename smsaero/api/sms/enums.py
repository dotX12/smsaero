from enum import Enum


class SMSStatus(int, Enum):
    IN_QUEUE = 0
    SUCCESS = 1
    ERROR = 2
    TRANSFER = 3
    WAITING_STATUS = 4
    REJECT = 6
    MODERATION = 8


class SMSChannel(str, Enum):
    FREE_SIGN = "FREE SIGN"
    PAY_SIGN = "PAY SIGN"
    SERVICE = "SERVICE"


class SmsURL:
    SEND = "v2/sms/send"
