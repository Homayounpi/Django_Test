import unittest
from Mock.m import get_apple
# from Mock.m import rm,
import os
from unittest import mock
from requests.exceptions import Timeout
from .m import requests


# class TestRm(unittest.TestCase):
#     filename = 'a.txt'

#     @mock.patch('main.os.remove')
#     def test_rm(self,mock_rm):
#         rm(self.filename)
#         self.assertFalse(os.path.isfile(self.filename))


#===========================================================================

class TestApple(unittest.TestCase):
    @mock.patch.object(requests,'get',side_effect=Timeout)
    def test_get_apple_timeout(self,mock_request):
        # mock_request.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_apple()

