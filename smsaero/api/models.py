from typing import Optional
from pydantic import BaseModel


class BaseResponseModel(BaseModel):
    success: bool
    message: Optional[str] = None
