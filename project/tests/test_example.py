# project/tests/test_example.py


import unittest

from project.tests.base import BaseTestCase


class TestExample(BaseTestCase):
    def test_example(self):
        self.assertTrue(True == True)


if __name__ == '__main__':
    unittest.main()
