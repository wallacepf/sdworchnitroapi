from sdworchnitroapi import auth_controller
from sdworchnitroapi import version_controller

ccId = '9ykds9mj1ll1'
clientId = '23881f3b-31cd-4fe7-9859-f61499dc9159'
clientSecret = 'ZberPqH5PM6qPjfDpUZ7Pw=='

connection = auth_controller.Auth(ccId, clientId, clientSecret)
token = connection.logon()['token']


def test_login():
    assert token.startswith('CWSAuth bearer')


def test_logout():
    assert connection.logoff(token) == True
    assert connection.logoff(token) != True
