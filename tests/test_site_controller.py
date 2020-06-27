from sdworchnitroapi import auth_controller as ac
from sdworchnitroapi import site_controller as sc

import os
import json
import pytest

cc_id = os.environ('CCID')
client_id = os.environ('CLIENT_ID')
client_secret = os.environ('CLIENT_SECRET')
customer_id = os.environ('CUSTOMER_ID')

connection = ac.Auth(cc_id, client_id, client_secret)
token = connection.logon()['token']

site_mgmt = sc.SiteController(cc_id, customer_id)


@pytest.fixture
def site_scope():
    payload_mcn = {
        "address": "Rua Joao Martins Bueno, 68",
        "applianceMode": "primary_ncn",
        "bandwidthTier": 100,
        "edition": "SE",
        "model": "cbvpx",
        "name": "MCN01-A",
        "subModel": "BASE"
    }

    payload_client = {
        "address": "Citrix Systems",
        "applianceMode": "client",
        "bandwidthTier": 50,
        "edition": "SE",
        "model": "210",
        "name": "SITE01",
        "subModel": "BASE"
    }

    return payload_mcn, payload_client


@pytest.fixture
def modify_site_address():
    payload = {
        "address": "Python Lib Test, 123"
    }
    return payload


@pytest.fixture
def get_site_infos():
    site_id = site_mgmt.get_sites()[0]['activeDevice']['id']
    updated_at = site_mgmt.get_sites()[0]['activeDevice']['updatedAt']
    return site_id, updated_at


def test_create_site(site_scope):
    result_mcn = site_mgmt.create_site(site_config=site_scope[0])
    result_client = site_mgmt.create_site(site_config=site_scope[1])
    assert result_mcn['createdAt']
    assert result_client['createdAt']


def test_get_sites():
    assert site_mgmt.get_sites()[0]['activeDevice']['createdAt']


def test_get_site(get_site_infos):
    assert site_mgmt.get_site(site_id=get_site_infos[0])[
        'activeDevice']['id'] == get_site_infos[0]


def test_del_site(get_site_infos):
    pass


def test_modify_site(modify_site_address, get_site_infos):
    assert site_mgmt.modify_site(site_id=get_site_infos[0], site_config=modify_site_address)[
        'activeDevice']['createdAt'] != get_site_infos[1]
