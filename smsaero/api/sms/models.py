import datetime
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel, Field

from smsaero.api.models import BaseResponseModel
from smsaero.api.sms.enums import SMSChannel
from smsaero.api.sms.enums import SMSStatus


class ErrorValidationModel(BaseModel):
    sign: Optional[List[str]]
    number: Optional[List[str]]
    text: Optional[List[str]]


class SMSSendResponseModel(BaseModel):
    id: int
    from_: str = Field(..., alias='from')
    number: str
    text: str
    status: SMSStatus
    extendStatus: str
    channel: SMSChannel
    cost: float

    time_create: datetime.datetime = Field(..., alias="dateCreate")
    time_update: datetime.datetime = Field(..., alias="dateSend")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class GetSMSResponse(BaseResponseModel):
    data: SMSSendResponseModel
