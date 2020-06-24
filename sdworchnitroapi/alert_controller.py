import requests
import json


class AlertController:
    def __init__(self, ccId, customerId, token, **kwargs):
        self.ccId = ccId
        self.customerId = customerId
        self.alertIds = kwargs.get(
            'alertIds') if kwargs.get('alertIds') else None
        self.siteId = kwargs.get('siteId') if kwargs.get('siteId') else None
        self.mspId = kwargs.get('mspId') if kwargs.get('mspId') else None
        self.apiUrl = "https://sdwan-policy.citrixnetworkapi.net/"
        self.headers = {'Content-type': 'application/json',
                        'Authorization': token}

    def del_single_alerts(self, context="", alert_id=""):
        return self.__api_call_del(context=context, alert_id=alert_id)

    def get_alerts(self, context="", **kwargs):
        return self.__api_call_get(context=context, **kwargs)

    def del_all_alerts_customer(self):
        pass

    def get_alerts_count_customer(self):
        pass

    def get_alerts_site(self):
        pass

    def del_all_alerts_site(self):
        pass

    def get_alerts_count_site(self):
        pass

    def get_alerts_msp(self):
        pass

    def del_all_alerts_msp(self):
        pass

    def get_alerts_count_msp(self):
        pass

    def __api_call_get(self, context="", **kwargs):
        if context == "customer" or context == "":
            # Analyze the proper way to work with Group
            if kwargs.get('group'):
                request_ref = self.apiUrl + \
                    "%s/api/v1/customer/%s/alerts?group=%s" % (self.ccId,
                                                               self.customerId, kwargs.get('group'))
            else:
                request_ref = self.apiUrl + \
                    "%s/api/v1/customer/%s/alerts" % (self.ccId,
                                                      self.customerId)
                response = requests.get(request_ref, headers=self.headers)
        elif context == "site":
            request_ref = self.apiUrl + \
                "%s/api/v1/customer/%s/site/%s/alerts" % (self.ccId,
                                                          self.customerId, kwargs.get('site_id'))
            response = requests.get(request_ref, headers=self.headers)
        elif context == "msp":
            pass

        return response.json()

    def __api_call_del(self, context="", **kwargs):
        if context == "customer":
            request_ref = self.apiUrl + \
                "%s/api/v1/customer/%s/alert/%s" % (
                    self.ccId, self.customerId, kwargs.get('alert_id'))
            response = requests.delete(request_ref, headers=self.headers)
        elif context == "site":
            pass
        elif context == "msp":
            pass

        return response if response.status_code == 204 else False
