from sdworchnitroapi import auth_controller
from sdworchnitroapi import version_controller

import json
import os

cc_id = os.environ['CCID']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

connection = auth_controller.Auth(cc_id, client_id, client_secret)
token = connection.logon()['token']

versions = version_controller.VersionController(cc_id, token)
key_list = ['dnbuTrust', 'statsCollector', 'configCompiler', 'home',
            'diagnostics', 'download',
            'saasGw', 'applmgr', 'location',
            'resourceProvider', 'config', 'appRouting',
            'reporting', 'licensing', 'policy']


def test_get_health():
    json_return = versions.get_health()
    for each in key_list:
        assert each in json_return
    assert len(key_list) == len(versions.get_health())

# Bug fix pending


def test_get_service_versions():
    pass


def test_get_version():
    assert versions.get_version()['version']
