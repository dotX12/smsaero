from typing import Optional
from typing import Type
from typing import TypeVar

from pydantic import BaseModel

from smsaero.rest.http import HTTPClient
from smsaero.settings import AuthSettings

T = TypeVar("T", bound=BaseModel)


class ServiceRequest(HTTPClient, AuthSettings):
    async def request(
        self,
        base_url: str,
        target_url: str,
        method: str,
        response_model: Optional[Type[T]] = None,
        **kwargs,
    ) -> T:
        prepare_url = self._prepare_url(
            email=self.email, api_key=self.api_key, base_url=base_url, url=target_url
        )
        response, _ = await self._request(
            method=method,
            url=prepare_url,
            **kwargs,
        )
        if response_model:
            response = response_model.parse_obj(response)
        return response
