import requests


class MakeRequest:
    def __init__(
        self,
        uri,
        method="GET",
        data=None,
        params=None,
        auth=None,
        app=None,
        headers=None,
    ):
        self.uri = uri
        self.data = data
        self.params = params
        self.method = method
        self.application = app
        self.auth = auth
        self.headers = {
            "Content-Type": "application/json",
        }
        if headers:
            self.headers.update(headers)

    def do_sync_request(self):
        with requests.Session() as session:
            response = session.request(
                self.method,
                self.uri,
                json=self.data,
                params=self.params,
                auth=self.auth,
                headers=self.headers,
            )
            response.raise_for_status()

            return response.json()
