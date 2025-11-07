from pydantic import HttpUrl

from .authenticator import Authenticator
from .http import HttpClient
from .url_builder import UrlBuilder

# _imports_

class OpenRemoteClient:
    __authenticator: Authenticator
    __url_builder: UrlBuilder
    __http_client: HttpClient

    # _attribute_definitions_

    def __init__(self, host: HttpUrl | str, client_id: str, client_secret: str, realm: str = 'master', verify_SSL: bool = True):
        self.__url_builder = UrlBuilder(host)
        self.__authenticator = Authenticator(self.__url_builder, client_id, client_secret, verify_SSL)
        self.__http_client = HttpClient(self.__url_builder, self.__authenticator, realm, verify_SSL)

        # Init API endpoints
        # _attribute_inits_

        # Init HTTPX Generic method
        self.get = self.__http_client.get
        self.post = self.__http_client.post
        self.put = self.__http_client.put
        self.delete = self.__http_client.delete

    def set_realm(self, realm: str):
        self.__http_client.set_realm(realm)
