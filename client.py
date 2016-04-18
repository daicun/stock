# client.py
# conding=utf-8
import httplib
import traceback
import urllib

class Client(object):
    sDomain = 'api.wmcloud.com'
    sPort   = 443
    sToken  = ''
    sClient = None
    def __init__(self):
        # self.sClient = httplib.HTTPConnection(self.sDomain, self.sPort)
        self.sClient = httplib.HTTPSConnection(self.sDomain, self.sPort)
    def __del__(self):
        if self.sClient is not None:
            self.sClient.close()
    def init(self, token):
        self.sToken = token
    def getData(self, path):
        result = None
        path   = '/data/v1' + path
        try:
            self.sClient.request('GET', path, headers = {"Authorization": "Bearer " + self.sToken})
            # self.sClient.request('GET', path, headers = {"Authorization": "Bearer " + self.sToken})
            response = self.sClient.getresponse()
            print 'response.status: ' + str(response.status)
            if response.status == 200:
                result = response.read()
            else:
                result = response.read()

            if path.find('.csv?') == -1:
                # result = result.decode('utf-8').encode('GB18030')
                result = result.decode('utf-8')
            return response.status, result
        except Exception as e:
            raise e
        return -1, result