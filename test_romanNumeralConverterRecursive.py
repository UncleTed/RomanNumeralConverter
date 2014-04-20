from unittest import TestCase
from RomanNumeralConverterRecursive import RomanNumeralConverterRecursive

__author__ = 'Ted Layher'


class TestRomanNumeralConverterRecursive(TestCase):
    def setUp(self):
        self.converter = RomanNumeralConverterRecursive()
        self.cr = self.converter.convert_roman

    def test_equals(self):
        self.assertEqual(1, 1, "one better equal one for ints")
        self.assertEqual(1.1, 1.1, "one point one for double")
        self.assertTrue(True)
        self.assertGreater(2, 1)
        self.assertLess(1, 2)

    def test_convert_the_easy_ones(self):
        numerals = ["I", "II", "III", "V", "VI", "VII", "VIII", "X", "XI", "XII", "XIII", "XV", "XVI", "XVII", "XVIII",
                    "XX", "XXVI", "XXX"]
        answers = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 20, 26, 30]
        for i in range(len(numerals)):
            self.assertEquals(answers[i], self.cr(numerals[i]), "failed at " + numerals[i])


    def test_hard(self):
        numerals = ["IV", "IX", "XL", "XC"]
        answers = [4, 9, 40, 90]
        for i in range(len(numerals)):
            self.assertEquals(answers[i], self.cr(numerals[i]), "failed on " + numerals[i])