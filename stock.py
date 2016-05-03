#/usr/bin/python
#
#-*- coding: utf-8 -*-

import httplib
import json
import sys

class Stock(object):
    # default host
    sHost = 'api.wmcloud.com'
    # default port
    sPort = 443
    #
    sHTTPSConnection = None
    #
    sToken = ''

    def __init__(self):
        self.sHTTPSConnection = httplib.HTTPSConnection(self.sHost, self.sPort)

    def __del__(self):
        if self.sHTTPSConnection is not None:
            self.sHTTPSConnection.close()

    def getEqu(self, field = '', listStatusCD = '', secID = '', ticker = '', equTypeCD = 'A'):
        # format
        path = '/data/v1' + '/api/equity/getEqu.json?field={0}&listStatusCD={1}&secID={2}&ticker={3}&equTypeCD={4}'.format(field, listStatusCD, secID, ticker, equTypeCD)
        #
        print 'path:' + path

        try:
            self.sHTTPSConnection.request('GET', path, headers = {'Authorization': 'Bearer ' + self.sToken})
            # get response object
            response = self.sHTTPSConnection.getresponse()
            # get json object
            jObject = response.read()
            # convert json obejct to python object
            pObejct = json.loads(jObject, encoding='utf-8')
            # get return code
            code = pObejct['retCode']
            # get return messages
            msg  = pObejct['retMsg']
            # get return data
            data = pObejct['data']

            # print 'code:        ' + str(code)
            # print 'messages:    ' + msg
            # print 'data length: ' + str(len(data))

            # return python object
            return data
            # return None
        except Exception as e:
            raise e

        return None
