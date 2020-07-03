import requests
import json


class AlertController:
    def __init__(self, cc_id, token):
        self.cc_id = cc_id
        self.api_url = "https://sdwan-policy.citrixnetworkapi.net/{}/api/v1/".format(
            cc_id)
        self.headers = {'Content-type': 'application/json',
                        'Authorization': token}

    def get_alerts(self, **kwargs):
        return self.__api_call_get(**kwargs)

    def del_alert(self, **kwargs):
        return self.__api_call_del(**kwargs)

    def del_all_alerts(self, **kwargs):
        return self.__api_call_del_all(**kwargs)

    def get_alert_count(self, **kwargs):
        return self.__api_call_get_count(**kwargs)

    def __api_call_get(self, **kwargs):
        if kwargs.get('customer_id'):
            request_ref = self.api_url + \
                'customer/{}/alerts'.format(kwargs.get('customer_id'))
            response = requests.get(request_ref, headers=self.headers)
        elif kwargs.get('customer_id') and kwargs.get('site_id'):
            request_ref = self.api_url + \
                'customer/{}/site/{}/alerts'.format(
                    kwargs.get('customer_id'), kwargs.get('site_id'))
            response = requests.get(request_ref, headers=self.headers)
        elif kwargs.get('msp_id'):
            request_ref = self.api_url + \
                'msp/{}/alerts'.format(kwargs.get('msp_id'))
            response = requests.get(request_ref, headers=self.headers)
        
        return response.json()

    def __api_call_del(self, **kwargs):
        if kwargs.get('customer_id') and kwargs.get('alert_id'):
            request_ref = self.api_url + \
                'customer/{}/alert/{}'.format(kwargs.get(
                    'customer_id'), kwargs.get('alert_id'))
            response = requests.delete(request_ref, headers=self.headers)
        elif kwargs.get('msp_id') and kwargs.get('alert_id'):
            request_ref = self.api_url + \
                'msp/{}/alert/{}'.format(kwargs.get('msp_id'),
                                         kwargs.get('alert_id'))
            response = requests.delete(request_ref, headers=self.headers)

        return 'Done' if response.status_code == 204 else False

    def __api_call_del_all(self, **kwargs):
        if kwargs.get('customer_id'):
            requests_ref = self.api_url + \
                'customer/{}/alerts'.format(kwargs.get('customer_id'))
            response = requests.delete(requests_ref, headers=self.headers)
        elif kwargs.get('customer_id') and kwargs.get('site_id'):
            requests_ref = self.api_url + \
                'customer/{}/site/{}/alerts'.format(
                    kwargs.get('customer_id'), kwargs.get('site_id'))
            response = requests.delete(requests_ref, headers=self.headers)
        elif kwargs.get('msp_id'):
            requests_ref = self.api_url + \
                'msp/{}/alerts'.format(kwargs.get('msp_id'))
            response = requests.delete(requests_ref, headers=self.headers)

        return 'Done' if response.status_code == 204 else False

    def __api_call_get_count(self, **kwargs):
        if kwargs.get('customer_id'):
            requests_ref = self.api_url + \
                'customer/{}/alerts/count'.format(kwargs.get('customer_id'))
            response = requests.get(requests_ref, headers=self.headers)
        elif kwargs.get('customer_id') and kwargs.get('site_id'):
            requests_ref = self.api_url + \
                'customer/{}/site/{}/alerts/count'.format(
                    kwargs.get('customer_id'), kwargs.get('site_id'))
            response = requests.get(requests_ref, headers=self.headers)
        elif kwargs.get('msp_id'):
            requests_ref = self.api_url + \
                'msp/{}/alerts/count'.format(kwargs.get('msp_id'))
            response = requests.get(requests_ref, headers=self.headers)

        return response.json()
