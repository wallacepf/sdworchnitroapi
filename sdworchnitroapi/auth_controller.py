import requests
import json


class Auth:

    def __init__(self, cc_id, client_id, client_secret):
        self.cc_id = cc_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_url = "https://sdwan-policy.citrixnetworkapi.net/"

    def logon(self):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "ccId": self.cc_id,
            "clientId": self.client_id,
            "clientSecret": self.client_secret
        }

        return self.__api_call('logon', headers, payload=payload)

    def logoff(self, token):
        headers = {'Content-type': 'application/json', 'Authorization': token}
        return self.__api_call('logoff', headers)

    def __api_call(self, uri, headers, **kwargs):
        request_ref = self.api_url + "%s/api/v1/%s" % (
            self.cc_id, uri)
        if kwargs.get('payload'):
            response = requests.post(
                request_ref, headers=headers, data=json.dumps(kwargs.get('payload')))
        else:
            response = requests.post(
                request_ref, headers=headers)

        return response.json()
