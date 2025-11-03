from httpx import Response

from ..http import HttpClient
from ..schemas.external_service import ExternalService


class Services:
    __client: HttpClient

    def __init__(self, client: HttpClient):
        self.__client = client

    async def register_global(self, external_service: ExternalService) -> ExternalService:
        response = await self.__client.post(f'/service/global', json=external_service.model_dump())

        return ExternalService(**response.json())


    async def heartbeat(self, serviceId: str, instanceId: int):
        return await self.__client.put(f'/service/{serviceId}/{instanceId}')
