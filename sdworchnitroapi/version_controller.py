import requests
import json


class AlertController:

    def __init__(self, ccId, token):
        self.ccId = ccId
        self.token = token
        self.apiUrl = "https://sdwan-policy.citrixnetworkapi.net/"

    def getHealth(self):
        return self.__apiCall('health')

    def getServiceVersions(self):
        return self.__apiCall('serviceVersions')

    def getVersion(self):
        return self.__apiCall('version')

    def __apiCall(self, uri):
        request_ref = self.apiUrl + "%s/api/v1/%s" % (self.ccId, uri)

        response = requests.get(request_ref)
        return response.json()
