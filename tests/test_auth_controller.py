from sdworchnitroapi import auth_controller

import os

cc_id = os.environ['CCID']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

connection = auth_controller.Auth(cc_id, client_id, client_secret)
token = connection.logon()['token']


def test_login():
    assert token.startswith('CWSAuth bearer')


def test_logout():
    assert connection.logoff(token) == True
    assert connection.logoff(token) != True
