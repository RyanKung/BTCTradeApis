# -*- coding: utf-8 -*-
import sys
import os
import random
import datetime
import httplib
import urllib
import json
import hashlib
import hmac
import time

class Trader:

    API_KEY = ''
    API_SECRET = ''
    tradeHistroyBuffer = []

    def __init__(self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET

    def signature(self, params):
        return hmac.new(self.API_SECRET, params, digestmod=hashlib.sha512).hexdigest()

    def getData(self, uri, params = {}):
        data = {}
        params = urllib.urlencode(params)
        conn = httplib.HTTPSConnection("btc-e.com")
        headers = {"Content-type" : "application/x-www-form-urlencoded",
                   "Key" : self.API_KEY,
                   "sign" : self.signature(params)}
        while 1:
            try:
                conn.request("GET", uri, params, headers)
                response = conn.getresponse()
                data = json.load(response)
                conn.close()
                break
            except KeyboardInterrupt:
                sys.exit()
            except:
                print "Network Error."
        return data
     
    def callAPI(self, params = {}):
        data = {}
        params['nonce'] = str(time.time()).split('.')[0]
        params = urllib.urlencode(params)
        conn = httplib.HTTPSConnection("btc-e.com")
        headers = {"Content-type" : "application/x-www-form-urlencoded",
                   "Key" : API_KEY,
                   "sign" : signature(params)}
        while 1:
            try:
                conn.request("POST", '/tapi', params, headers)
                response = conn.getresponse()
                data = json.load(response)
                conn.close()
                break
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Network Error.")
        return data
    

#PRICE INFO
    def getTrade(self, type):
        api = "/api/2/%s/trades"%type
        data = self.getData(api)
        return data
     
    def getDepth(self, type):
        api = "/api/2/%s/depth"%type
        data = self.getData(api)
        return data
     
    def getTicker(self, type):
        api = "/api/2/%s/ticker"%type
        data = self.getData(api)
        return data['ticker']
     
    def getFee(self, type):
        api = "/api/2/%s/fee"%type
        data = self.getData(api)
        return data
     
    #TRADE INFO
    def getTradeInfo(self):
        params = {}
        params['method'] = 'getInfo'
        data = self.callAPI(params)
        return data
     
    def getTransHistory(self):
        params = {}
        params['method'] = 'TransHistory'
        data = self.callAPI(params)
        return data
     
    def getTradeHistory(self ):
        params = {}
        params['method'] = 'TradeHistory'
        data = self.callAPI(params)
        return data
     
    def getOrderList(self):
        params = {}
        params['method'] = 'OrderList'
        data = self.callAPI(params)
        return data
     
    def getActiveOrders(self, pair = 'btc_usd'):
        params = {}
        params['method'] = 'ActiveOrders'
        params['pair'] = pair
        data = self.callAPI(params)    
        return data
     
    # TRADE API
    def doTrade(self, pair, type, rate, amount):
        params = {}
        params['method'] = 'trade'
        params['pair'] = pair
        params['type'] = type # buy or sell
        params['rate'] = rate
        params['amount'] =amount
        data = self.callAPI(params)
        return data
     
    def sell(self, rate, amount):
        self.doTrade(TYPE, 'sell', rate, amount)
     
    def buy(self, pair, rate, amount):
        self.doTrade(TYPE, 'buy', rate, amount)
     
    def cancelOrder(self, order_id):
        params = {}
        params['method'] = 'cancelOrder'
        params['order_id'] = order_id
        data = self.callAPI(params)    
        return data

    def getLastTrade(self):
        return self.tradeHistroyBuffer[-1]

