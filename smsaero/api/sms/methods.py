from smsaero.api.misc import SMSAeroURL
from smsaero.api.sms.enums import SmsURL
from smsaero.api.sms.models import GetSMSResponse
from smsaero.services.request import ServiceRequest


class SMSService(ServiceRequest):
    async def send(
        self,
        phone: int,
        sign: str,
        text: str,
    ) -> GetSMSResponse:
        return await self.request(
            base_url=SMSAeroURL.BASE,
            target_url=SmsURL.SEND,
            method="GET",
            params={
                "number": phone,
                "sign": sign,
                "text": text,
            },
            response_model=GetSMSResponse,
        )

