from sdworchnitroapi import alert_controller
from sdworchnitroapi import auth_controller

import os
import json

cc_id = os.environ['CCID']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
customer_id = os.environ['CUSTOMER_ID']
msp_id = os.environ['MSP_ID']

connection = auth_controller.Auth(cc_id, client_id, client_secret)
token = connection.logon()['token']

alerts = alert_controller.AlertController(cc_id, customer_id, token, msp_id)

key_list = ['createdAt', 'customerId', 'customerName', 'deviceId', 'id', 'message', 'networkId', 'objectName',
            'objectType', 'severity', 'siteId', 'siteName', 'source', 'state', 'time', 'updatedAt', 'userSeverity']


class GetAlerts:
    def test_get_alerts_customer(self):
        json_return = json.dumps(alerts.get_alerts(context='customer'))
        for each in key_list:
            assert each in json_return['alerts'][0]
        assert 'totalElements' in json_return
        assert len(key_list) == len(
            alerts.get_alerts(context='customer').keys())

    def test_get_alerts_site(self):
        pass

    def test_get_alerts_msp(self):
        pass


class DelAlert:
    def test_del_alert_customer(self):
        pass

    def test_del_alert_msp(self):
        pass


class DelAllAlerts:
    def test_del_all_alerts_customer(self):
        pass

    def test_del_all_alerts_site(self):
        pass

    def test_del_all_alerts_msp(self):
        pass


class GetAlertCount:
    def test_get_alert_count_customer(self):
        pass

    def test_get_alert_count_site(self):
        pass

    def test_get_alert_count_msp(self):
        pass


# def test_del_single_alert_contextual():
#     assert alerts.del_all_alerts(
#         context='customer', alert_id='') == 'Done'
#     assert alerts.del_all_alerts(context='msp', alert_id='') == 'Done'
