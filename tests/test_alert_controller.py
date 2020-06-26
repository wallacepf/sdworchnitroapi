from sdworchnitroapi import alert_controller
from sdworchnitroapi import auth_controller

import os
import json
import pytest

cc_id = os.environ['CCID']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
customer_id = os.environ['CUSTOMER_ID']
site_id = os.environ['SITE_ID']
msp_id = os.environ['MSP_ID']

connection = auth_controller.Auth(cc_id, client_id, client_secret)
token = connection.logon()['token']

alerts = alert_controller.AlertController(
    cc_id, token)

key_list = ['createdAt', 'customerId', 'customerName', 'deviceId', 'id', 'message', 'networkId', 'objectName',
            'objectType', 'severity', 'siteId', 'siteName', 'source', 'state', 'time', 'updatedAt', 'userSeverity']


class GetAlerts:
    def test_get_alerts_customer(self):
        json_return = json.dumps(alerts.get_alerts())
        for each in key_list:
            assert each in json_return['alerts'][0]
        assert 'totalElements' in json_return
        assert len(key_list) == len(
            alerts.get_alerts(customer_id=customer_id).keys())

    def test_get_alerts_site(self):
        json_return = json.dumps(alerts.get_alerts(site_id=site_id))
        for each in key_list:
            assert each in json_return['alerts'][0]
        assert 'totalElements' in json_return
        assert len(key_list) == len(
            alerts.get_alerts(site_id=site_id).keys())

    def test_get_alerts_msp(self):
        json_return = json.dumps(alerts.get_alerts(msp_id=msp_id))
        for each in key_list:
            assert each in json_return['alerts'][0]
        assert 'totalElements' in json_return
        assert len(key_list) == len(
            alerts.get_alerts(msp_id=msp_id).keys())


class DelAlert:
    @pytest.fixture
    def get_alert_data(self, **kwargs):
        id_return = alerts.get_alerts(**kwargs)['alerts'][0]['id']
        return id_return

    def test_del_alert_customer(self):
        alert_id = self.get_alert_data(customer_id=customer_id)
        assert alerts.del_alert(
            customer_id=customer_id, alert_id=alert_id) == 'Done'

    def test_del_alert_msp(self):
        alert_id = self.get_alert_data(msp_id=msp_id)
        assert alerts.del_alert(
            msp_id=msp_id, alert_id=alert_id) == 'Done'


class DelAllAlerts:
    def test_del_all_alerts_customer(self):
        assert alerts.del_all_alerts() == 'Done'

    def test_del_all_alerts_site(self):
        assert alerts.del_all_alerts(site_id=site_id) == 'Done'

    def test_del_all_alerts_msp(self):
        assert alerts.del_all_alerts(site_id=site_id) == 'Done'


class GetAlertCount:
    def test_get_alert_count_customer(self):
        assert alerts.get_alert_count(customer_id=customer_id)[
            'alertsCount'][0]['count'] >= 0

    def test_get_alert_count_site(self):
        assert alerts.get_alert_count(site_id=site_id)[
            'alertsCount'][0]['count'] >= 0

    def test_get_alert_count_msp(self):
        assert alerts.get_alert_count(msp_id=msp_id)[
            'alertsCount'][0]['count'] >= 0
