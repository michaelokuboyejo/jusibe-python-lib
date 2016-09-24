from jusibe.core import Jusibe
from jusibe.exceptions import ServiceError, BadRequestError
from keys import PUBLIC_KEY, ACCESS_TOKEN

__author__ = 'michaelokuboyejo'

import unittest

from unittest import TestCase


class BaseTest(TestCase):
    """ A Base Test Case Class"""

    def setUp(self):
        self.jusibe = Jusibe

    def tearDown(self):
        self.jusibe = Jusibe

    def test_network_error_raises_connection_exception(self):
        self.jusibe = Jusibe(PUBLIC_KEY, ACCESS_TOKEN)
        self.jusibe.perform_get_request('http://qwertyui.qwerty')
        self.assertRaises(ServiceError)

    def test_empty_key_values_raises_bad_request_exception(self):
        self.jusibe = Jusibe("","")
        self.assertRaises(BadRequestError)


if __name__ == '__main__':
    unittest.main()
