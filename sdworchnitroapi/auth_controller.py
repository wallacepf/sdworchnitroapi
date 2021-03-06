import requests
import json


class Auth:

    def __init__(self, ccId, clientId, clientSecret):
        self.ccId = ccId
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.apiUrl = "https://sdwan-policy.citrixnetworkapi.net/"

    def logon(self):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "ccId": self.ccId,
            "clientId": self.clientId,
            "clientSecret": self.clientSecret
        }

        return self.__apiCall('logon', headers, payload=payload)

    def logoff(self, token):
        headers = {'Content-type': 'application/json', 'Authorization': token}
        return self.__apiCall('logoff', headers)

    def __apiCall(self, uri, headers, **kwargs):
        request_ref = self.apiUrl + "%s/api/v1/%s" % (
            self.ccId, uri)
        #Alterar os requests para request.post
        if kwargs.get('payload'):
            response = requests.request(
                "POST", request_ref, headers=headers, data=json.dumps(kwargs.get('payload')))
        else:
            response = requests.request(
                "POST", request_ref, headers=headers)

        return response.json()
