from pydantic import HttpUrl

from .authenticator import Authenticator
from .http import HttpClient
from .url_builder import UrlBuilder

from .api.asset import Asset
from .api.status import Status
from .api.services import Services


class OpenRemoteClient:
    __authenticator: Authenticator
    __url_builder: UrlBuilder
    __http_client: HttpClient

    asset: Asset
    status: Status

    def __init__(self, host: HttpUrl | str, client_id: str, client_secret: str, realm: str = 'master', verify_SSL: bool = True):
        self.__url_builder = UrlBuilder(host)
        self.__authenticator = Authenticator(self.__url_builder, client_id, client_secret, verify_SSL)
        self.__http_client = HttpClient(self.__url_builder, self.__authenticator, realm, verify_SSL)

        # Init API endpoints
        self.asset = Asset(self.__http_client)
        self.status = Status(self.__http_client)
        self.services = Services(self.__http_client)

        # Init HTTPX Generic method
        self.get = self.__http_client.get
        self.post = self.__http_client.post
        self.put = self.__http_client.put
        self.delete = self.__http_client.delete

    def set_realm(self, realm: str):
        self.__http_client.set_realm(realm)
