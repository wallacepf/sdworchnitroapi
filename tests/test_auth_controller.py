from sdworchnitroapi import auth_controller

import os

ccId = os.environ['CCID']
clientId = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

connection = auth_controller.Auth(ccId, clientId, clientSecret)
token = connection.logon()['token']


def test_login():
    assert token.startswith('CWSAuth bearer')


def test_logout():
    assert connection.logoff(token) == True
    assert connection.logoff(token) != True
