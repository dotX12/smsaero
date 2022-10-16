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
        response_model: Type[T],
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
        result_model = response_model.parse_obj(response)
        return result_model
