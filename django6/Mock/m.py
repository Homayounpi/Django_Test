import os
import datetime
from unittest.mock import Mock
import requests
import unittest
from unittest.mock import Mock
from requests.exceptions import Timeout


tuesday = datetime.datetime(year=2019,month=1,day=1)
sunday = datetime.datetime(year=2019,month=1,day=6)

datetime = Mock()
def is_weekday():
    today = datetime.datetime.today()
    return (0 <= today.weekday() <6)

datetime.datetime.today.return_value = tuesday
assert is_weekday()
datetime.datetime.today.return_value = sunday
assert is_weekday()


requests = Mock()

def get_apple():
    r = requests.get('https://www.apple.com')
    return r.status_code

class TestApple(unittest.TestCase):
    def test_get_apple_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_apple()

def get_apple():
    r = requests.get('https://www.apple.com')
    return r.status_code

