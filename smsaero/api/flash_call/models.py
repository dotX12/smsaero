import datetime
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel, Field

from smsaero.api.flash_call.enums import FlashCallStatus
from smsaero.api.models import BaseResponseModel


class ErrorValidationModel(BaseModel):
    code: Optional[List[str]]
    phone: Optional[List[str]]


class FlashCallSendDataModel(BaseModel):
    id: int
    status: FlashCallStatus
    code: str
    phone: str
    cost: float
    time_create: datetime.datetime = Field(..., alias="timeCreate")
    time_update: datetime.datetime = Field(..., alias="timeUpdate")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class FlashCallSendModel(BaseResponseModel):
    data: Union[FlashCallSendDataModel, ErrorValidationModel]


class FlashCallGetOneModel(FlashCallSendModel):
    pass


class FlashCallGetAllDataModel(BaseModel):
    content: List[FlashCallSendDataModel] = Field(..., alias="list")
    count: int = Field(..., alias="totalCount")


class FlashCallGetAllModel(BaseResponseModel):
    data: FlashCallGetAllDataModel
