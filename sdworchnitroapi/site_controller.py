import requests
import json


class SiteController():
    def __init__(self, cc_id, customer_id, token):
        self.api_url = "https://sdwan-policy.citrixnetworkapi.net/{}/api/v1/customer/{}/".format(
            cc_id, customer_id)
        self.headers = {'Content-type': 'application/json',
                        'Authorization': token}

    def create_site(self, site_config: dict):
        return self.__api_get_create(site_config)

    def get_site(self, site_id: str):
        return self.__api_get_site(site_id)

    def __api_get_create(self, site_config: dict):
        request_ref = self.api_url + "siteapi"
        response = requests.post(
            request_ref, headers=self.headers, data=json.dumps(site_config))
        return response.json()

    def __api_get_site(self, site_id: str):
        request_ref = self.api_url + 'site/{}'.format(site_id)
        response = requests.get(request_ref, headers=self.headers)
        return response.json()