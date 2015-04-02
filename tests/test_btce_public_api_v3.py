# -*- coding: utf-8 -*-

from tests import TestCase
from BTCTradeApis import btce

class TestBTCEPublicApiV3(TestCase):

    def setUp(self):
        self.api = btce.PublicApiV3()
        
    def test_methods(self, pairs='btc_usd'):

        def call_methods(fn, pair):
            '''
            call spec methods
            '''
            return getattr(self.api, fn)(pair)

        def test_methods(res):
            self.assertTrue(res.ok)
            self.assertEqual(res.status_code, '200')
            self.assertTrue(res.data)
            
        return map(lambda m:test_methods(call_method(m, pairs)), self.api.methods)
         

    def test_pairs(self):
        return self.test_methods(pairs=self.api.all_pairs)
