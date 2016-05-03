#/usr/bin/python
#
#-*- coding: utf-8 -*-

import sys
import json

from stock import Stock

def main():
    # try:
    #     sStock = Stock()
    #     code , result = sStock.getEqu(ticker = '000786')
    #     jDict = json.loads(result, encoding='utf-8')
    #     print 'jDict ticker: ' + jDict['data'][0]['ticker']
    #     print 'jDict officeAddr: ' + jDict['data'][0]['officeAddr'].encode('utf-8')
    # except Exception as e:
    #     raise e
    s = Stock()

    data = s.getEqu()
    if data is None:
        print 'get data object is failed'
    else:
        # print 'secID:           ' + data[0]['secID']
        # print 'ticker:          ' + data[0]['ticker']
        # print 'primeOperating:  ' + data[0]['primeOperating']
        # print 'TShEquity:       ' + str(data[0]['TShEquity'])
        for i in range(len(data)):
            print data[i]['secID'] + ': ' + data[i]['secShortName'] + ': ' + str(data[i]['TShEquity'])

if __name__ == '__main__':
    sys.exit(int(main() or 0))
