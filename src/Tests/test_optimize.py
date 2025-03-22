import unittest

from optimize import optimize
from Tests.settings import API_INPUT


class TestOptimize(unittest.TestCase):
    def test_optimize(self) -> None:
        optimize(API_INPUT)
