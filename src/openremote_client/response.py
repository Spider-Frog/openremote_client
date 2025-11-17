from typing import TypeVar, Generic

from httpx import Response
from pydantic import BaseModel, ConfigDict

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    status_code: int
    content: T
    response: Response

    model_config = ConfigDict(arbitrary_types_allowed=True)