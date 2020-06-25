from sdworchnitroapi import auth_controller
from sdworchnitroapi import version_controller

import json
import os

ccId = os.environ['CCID']
clientId = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

connection = auth_controller.Auth(ccId, clientId, clientSecret)
token = connection.logon()['token']

versions = version_controller.VersionController(ccId, token)
key_list = ['dnbuTrust', 'statsCollector', 'configCompiler', 'home',
            'diagnostics', 'download',
            'saasGw', 'applmgr', 'location',
            'resourceProvider', 'config', 'appRouting',
            'reporting', 'licensing', 'policy']


def test_get_health():
    json_return = json.dumps(versions.get_health())
    for each in key_list:
        assert each in json_return
    assert len(key_list) == len(versions.get_health().keys())


def test_get_service_versions():
    pass


def test_get_version():
    pass
