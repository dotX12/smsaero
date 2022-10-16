from smsaero.api.flash_call.enums import FlashCallURL
from smsaero.api.flash_call.models import FlashCallGetAllModel
from smsaero.api.flash_call.models import FlashCallGetOneModel
from smsaero.api.flash_call.models import FlashCallSendModel
from smsaero.api.misc import SMSAeroURL
from smsaero.services.request import ServiceRequest


class FlashCallService(ServiceRequest):
    async def send(
        self,
        phone: int,
        code: str,
    ) -> FlashCallSendModel:
        return await self.request(
            base_url=SMSAeroURL.BASE,
            target_url=FlashCallURL.SEND,
            method="GET",
            params={"phone": phone, "code": code},
            response_model=FlashCallSendModel,
        )

    async def get_one(self, _id: int) -> FlashCallGetOneModel:
        return await self.request(
            base_url=SMSAeroURL.BASE,
            target_url=FlashCallURL.GET_ONE,
            method="GET",
            params={"id": _id},
            response_model=FlashCallGetOneModel,
        )

    async def get_all(self) -> FlashCallGetAllModel:
        return await self.request(
            base_url=SMSAeroURL.BASE,
            target_url=FlashCallURL.GET_ALL,
            method="GET",
            response_model=FlashCallGetAllModel,
        )
