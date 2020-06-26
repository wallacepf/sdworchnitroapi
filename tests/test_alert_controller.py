from sdworchnitroapi import alert_controller
from sdworchnitroapi import auth_controller

import os
import json
import pytest

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
        json_return = json.dumps(alerts.get_alerts(context='site'))
        for each in key_list:
            assert each in json_return['alerts'][0]
        assert 'totalElements' in json_return
        assert len(key_list) == len(
            alerts.get_alerts(context='customer').keys())

    def test_get_alerts_msp(self):
        json_return = json.dumps(alerts.get_alerts(context='msp'))
        for each in key_list:
            assert each in json_return['alerts'][0]
        assert 'totalElements' in json_return
        assert len(key_list) == len(
            alerts.get_alerts(context='customer').keys())

class DelAlert:
    @pytest.fixture
    def get_alert_data_customer(self, context):
        id_return = alerts.get_alerts(context=context)['alerts'][0]['id']
        return id_return

    def test_del_alert_customer(self):
        assert alerts.del_alert(
            context='customer', alert_id=self.get_alert_data_customer('customer')) == 'Done'

    def test_del_alert_msp(self):
        assert alerts.del_alert(
            context='msp', alert_id=self.get_alert_data_customer('msp')) == 'Done'

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
