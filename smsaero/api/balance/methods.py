from smsaero.api.balance.enums import BalanceURL
from smsaero.api.balance.models import GetBalanceModel
from smsaero.api.misc import SMSAeroURL
from smsaero.services.request import ServiceRequest


class BalanceService(ServiceRequest):
    async def get(self) -> GetBalanceModel:
        return await self.request(
            base_url=SMSAeroURL.BASE,
            target_url=BalanceURL.BALANCE,
            method="GET",
            response_model=GetBalanceModel,
        )
