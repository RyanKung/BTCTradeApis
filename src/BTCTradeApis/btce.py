# -*- coding: utf-8 -*-
import requests

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


    class ApiResponse(object):
        pass
    @property
    def all_pairs(self):
        return '-'.join(self.pairs)
    
    def append_pairs(self, pairs):
        '''
        Add pair to exist pairs
        :param paris: accept list, tuple or str
        :return: self
        '''
        if type(pair) in [list, tuple]:
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
            return {'data': res.json(),
                    'ok': res.ok,
                    'status_code': res.status_code
            }
        
        def do_request():
            # list/str -> request
            
            if type(pairs) in [list, tuple]:
                return requests.get(self.api%(method, '-'.join(pairs)),
                                    data=kwargs,
                                    verify=True)
            else:
                return requests.get(self.api%(method, pairs),
                                    data=kwargs,
                                    verify=True)

        return response_handler(do_request())

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
            setattr(self, 'get_%s'%method,
                    lambda ps: self.call_method(method, ps))
            return self
        
        map(regist_apis, self.methods)
        
class TradeAPIV1:
    pass

