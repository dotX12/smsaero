from smsaero.api.auth.methods import AuthService
from smsaero.api.balance.methods import BalanceService
from smsaero.api.flash_call.methods import FlashCallService


class SMSAero:
    def __init__(self, email: str, api_key: str):
        self.flash_call = FlashCallService(email=email, api_key=api_key)
        self.auth = AuthService(email=email, api_key=api_key)
        self.balance = BalanceService(email=email, api_key=api_key)
