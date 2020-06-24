import requests
import json


class VersionController:

    def __init__(self, ccId, token):
        self.ccId = ccId
        self.token = token
        self.apiUrl = "https://sdwan-policy.citrixnetworkapi.net/"

    def get_health(self):
        return self.__api_call('health')

    def get_service_versions(self):
        return self.__api_call('serviceVersions')

    def get_version(self):
        return self.__api_call('version')

    def __api_call(self, uri):
        request_ref = self.apiUrl + "%s/api/v1/%s" % (self.ccId, uri)

        response = requests.get(request_ref)
        return response.json()
