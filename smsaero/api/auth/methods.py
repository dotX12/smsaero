from smsaero.api.auth.enums import AuthURL
from smsaero.api.auth.models import GetAuthModel
from smsaero.api.misc import SMSAeroURL
from smsaero.services.request import ServiceRequest


class AuthService(ServiceRequest):
    async def auth(self) -> GetAuthModel:
        return await self.request(
            base_url=SMSAeroURL.BASE,
            target_url=AuthURL.AUTH,
            method="GET",
            response_model=GetAuthModel,
        )
