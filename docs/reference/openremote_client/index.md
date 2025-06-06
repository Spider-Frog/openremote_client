Module openremote_client
========================

Sub-modules
-----------
* openremote_client.api
* openremote_client.authenticator
* openremote_client.http
* openremote_client.schemas
* openremote_client.url_builder

Classes
-------

`OpenRemoteClient(host: pydantic.networks.HttpUrl | str, client_id: str, client_secret: str, realm: str = 'master')`
:   

    ### Class variables

    `asset: openremote_client.api.asset.Asset`
    :   The type of the None singleton.

    `status: openremote_client.api.status.Status`
    :   The type of the None singleton.

    ### Methods

    `set_realm(self, realm: str)`
    :