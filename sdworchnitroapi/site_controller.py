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

    def get_sites(self):
        return self.__api_get_site(site_id='')

    def modify_site(self, site_id: str, site_config: dict):
        return self.__api_modify_site(site_id, site_config)

    def get_site_stats(self, site_id: str):
        return self.__api_get_site_stats(site_id)

    def get_site_with_features(self):
        return self.__api_get_site_with_features()

    def del_site(self, site_id: str):
        return self.__api_del_site(site_id)

    def __api_get_create(self, site_config: dict):
        request_ref = self.api_url + "siteapi"
        response = requests.post(
            request_ref, headers=self.headers, data=json.dumps(site_config))
        return response.json()

    def __api_get_site(self, site_id: str):
        if site_id != '':
            request_ref = self.api_url + 'site/{}'.format(site_id)
            response = requests.get(request_ref, headers=self.headers)
        else:
            request_ref = self.api_url + 'sites'
            response = requests.get(request_ref, headers=self.headers)
        return response.json()

    def __api_modify_site(self, site_id: str, site_config: dict):
        requests_ref = self.api_url + 'siteapi/{}'.format(site_id)
        response = requests.patch(
            requests_ref, headers=self.headers, data=json.dumps(site_config))
        return response.json()

    def __api_get_site_stats(self, site_id: str):
        requests_ref = self.api_url + 'site/{}/statistics'.format(site_id)
        response = requests.get(requests_ref, headers=self.headers)
        return response.json()

    def __api_get_site_with_features(self):
        requests_ref = self.api_url + 'site_features'
        response = requests.get(requests_ref, headers=self.headers)
        return response.json()

    def __api_del_site(self, site_id: str):
        requests_ref = self.api_url + 'site/{}'.format(site_id)
        response = requests.delete(requests_ref, headers=self.headers)
        return "Done" if response.status_code == 204 else response.json()
