import requests
import json


class VersionController:

    def __init__(self, cc_id, token):
        self.cc_id = cc_id
        self.token = token
        self.api_url = "https://sdwan-policy.citrixnetworkapi.net/"

    def get_health(self):
        return self.__api_call('health')

    def get_service_versions(self):
        return self.__api_call('serviceVersions')

    def get_version(self):
        return self.__api_call('version')

    def __api_call(self, uri):
        request_ref = self.api_url + "%s/api/v1/%s" % (self.cc_id, uri)

        response = requests.get(request_ref)
        return response.json()
