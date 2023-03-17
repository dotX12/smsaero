from smsaero.api.auth.methods import AuthService
from smsaero.api.balance.methods import BalanceService
from smsaero.api.sms.methods import SMSService


class SMSAero:
    def __init__(self, email: str, api_key: str):
        self.auth = AuthService(email=email, api_key=api_key)
        self.balance = BalanceService(email=email, api_key=api_key)
        self.sms = SMSService(email=email, api_key=api_key)
