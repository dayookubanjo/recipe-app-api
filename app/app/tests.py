"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc


class ViewTests(SimpleTestCase):
    def test_addition(self):
        res = calc.add(5, 7)
        self.assertEqual(res, 12)

    def test_subtract(self):
        res = calc.subtract(12, 4)
        self.assertEqual(res, 8)
