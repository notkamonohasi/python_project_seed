import unittest

from app import lambda_handler
from Tests.settings import HANDLER_BODY


class TestApp(unittest.TestCase):
    def test_app(self):
        lambda_handler(HANDLER_BODY)
