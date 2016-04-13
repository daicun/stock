#!python
import sys
from client import Client

sBasicInfo = ''

def main():
    print 'stock data analysis'
    print ''

    file = open("token.txt")
    try:
        tokenString = file.read()
    except Exception as e:
        raise e
    finally:
        file.close()

    token = tokenString[tokenString.find("=") + 1:]
    print 'token: ' + token
    
    url = '/api/macro/getChinaDataGDP.csv?field=&indicID=M010000002&indicName=&beginDate=&endDate='
    try:
        client = Client()
        client.init(token[token.find("=") + 1:])

        code, result = client.getData(url)
        if code == 200:
            print result
        else:
            print code
            print result
    except Exception as e:
        raise e

if __name__ == '__main__':
    sys.exit(int(main() or 0))