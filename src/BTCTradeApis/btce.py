# -*- coding: utf-8 -*-
import requests
import time


class PublicApiV3(object):
    '''
    doc : https://btc-e.com/api/3/docs
    '''

    # Api method list
    # class variable shared by all instances
    methods = ['info', 'ticker', 'depth', 'trades']
    pairs = ['btc_usd', 'btc_rur',
             'btc_eur', 'btc_cnh',
             'btc_gbp', 'ltc_btc',
             'ltc_usd', 'ltc_rur',
             'ltc_eur', 'ltc_cnh',
             'ltc_gpb', 'nmc_btc',
             'nmc_usd', 'nvc_btc',
             'nvc_usd', 'usd_rur',
             'eur_usd', 'eur_rur',
             'usd_cnh', 'gbd_usd',
             'ppc_btc', 'ppc_usd']

    # Api url https://btc-e.com/api/3/<method name>/<pair listing>
    api = "https://btc-e.com/api/3/%s/%s"

    def __init__(self):
        '''
        resgist api methods to the obj first
        '''
        def regist_apis(method):
            '''
            Construct and regist get_%method% api
            :param method: a method list
            :return: None
            '''
            setattr(self, 'get_%s' % method,
                    lambda ps: self.call_method(method, ps))
            return self
        [regist_apis(m) for m in self.methods]

    @property
    def all_pairs(self):
        return '-'.join(self.pairs)

    def append_pairs(self, pairs):
        '''
        Add pair to exist pairs
        :param paris: accept list, tuple or str
        :return: self
        '''
        if type(pairs) in [list, tuple]:
            self.pairs += pairs
        else:
            self.pairs.append(pairs)

    def call_method(self, method, pairs, *args, **kwargs):
        '''
        Call API Method
        :param method: method for the api
        :param **kwargs: other args for api calling
        :return: request response of api
        :rtype: dict
        '''
        def response_handler(res):
            # requestObj -> Dict
            assert res.status_code == 200, 'statusCode is %i' % res.status_code
            assert res.ok, 'Request Failed'
            return res.json()

        def do_request():
            # list/str -> request
            if type(pairs) in [list, tuple]:
                return requests.get(self.api % (method, '-'.join(pairs)),
                                    params=kwargs,
                                    verify=True)
            else:
                return requests.get(self.api % (method, pairs),
                                    params=kwargs,
                                    verify=True)

        try:
            return response_handler(do_request())
        except AssertionError as err:
            print(err)


class TradeAPIV1(object):
    '''
    doc: https://btc-e.com/tapi/docs
    All requests to Trade API come from the following
    URL: https://btc-e.com/tapi
    The method name is sent via the POST-parameter method.
    All method parameters are sent via the POST-parameters.
    All server responses are received in the JSON format.
    Each request needs an authentication..
    '''

    methods = ['getInfo',
               'Trade',
               'ActiveOrders',
               'OrderInfo',
               'CancelOrder',
               'TradeHistory',
               'TransHistory']

    api = 'https://btc-e.com/tapi'

    def __init__(self, key, sign):
        self.key = key
        self.sign = sign

        def regist_apis(method):
            '''
            Construct and regist get_%method% api
            :param method: a method list
            :return: None
            '''
            setattr(self, method,
                    lambda ps: self.call_method(method, ps))
            return self
        [regist_apis(m) for m in self.methods]

    @property
    def nonce(self):
        '''
        Second transaction
        For successful authentication you need to send a
        POST-parameter nonce with incremental numeric value for each request.
        Minimum nonce value - 1, maximum - 4294967294
        '''
        return int(time.time())

    @property
    def headers(self):
        return {'Key': self.key,
                'Sign': self.sign}

    @property
    def params(self):
        return {'nonce': self.nonce}

    def call_method(self, method, *args, **kwargs):

        def response_handler(res):
            # requestObj -> Dict
            assert res.status_code == 200, 'statusCode is %i' % res.status_code
            assert res.ok, 'Request Failed'
            return res.json()

        def do_request():
            requests.post(self.api, headers=self.headers,
                          data=dict(self.headers, **kwargs),
                          verify=True)

        try:
            return response_handler(do_request())
        except AssertionError as err:
            print(err)
