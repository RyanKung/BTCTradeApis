# -*- coding: utf-8 -*-

from tests import TestCase
from BTCTradeApis import btce

class TestBTCEPublicApiV3(TestCase):

    def setUp(self):
        self.api = btce.PublicApiV3()

    def test_get_info(self):
        res = self.api.get_info('btc_usd')
        self.assertTrue(res['ok'])
        self.assertEqual(res['status_code'], '200')
        self.assertTrue(res['data'])

    def test_pairs(self):
        res = self.api.get_info(self.api.all_pairs)
        self.assertTrue(res.ok)
        self.assertEqual(res.status_code, '200')
        self.assertTrue(res.data)

    def test_unsupport_pairs(self):
        pass

    def test_get_ticker(self):
        res = self.api.get_ticker('btc_usd')
        self.assertTrue(res.ok)
        self.assertEqual(res.status_code, '200')
        self.assertTrue(res.data)
        
