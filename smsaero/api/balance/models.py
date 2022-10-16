from pydantic import BaseModel

from smsaero.api.models import BaseResponseModel


class GetBalanceDataModel(BaseModel):
    balance: float


class GetBalanceModel(BaseResponseModel):
    data: GetBalanceDataModel
