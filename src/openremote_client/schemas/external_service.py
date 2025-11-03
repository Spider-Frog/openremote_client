from typing import Literal

from pydantic import BaseModel, Field


class ExternalService(BaseModel):
    realm: str | None = None
    isGlobal: bool | None = None
    serviceId: str = Field(min_length=3, max_length=255)
    instanceId: int | None = None
    version: str | None = None
    icon: str | None = None
    label: str
    homepageUrl: str
    status: Literal["AVAILABLE", "UNAVAILABLE"]
