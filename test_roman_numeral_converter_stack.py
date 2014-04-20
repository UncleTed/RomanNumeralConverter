__author__ = 'phred'
from unittest import TestCase
from RomanNumeralConverterStack import RomanNumeralConvertStack


class TestRomanNumeralConvertStack(TestCase):

    def setUp(self):
        self.converter = RomanNumeralConvertStack()

    def test_easy(self):
        roman = ["I", "II", "III", "V", "VI", "VIII", "X", "XV", "XVI", "XXX", "L", "C", "M"]
        answer = [1, 2, 3, 5, 6, 8, 10, 15, 16, 30, 50, 100, 1000]
        for i in range(len(roman)):
            self.assertEquals(answer[i], self.converter.convert(roman[i]), "failed on " + roman[i])

    def test_hard(self):
        roman = ["IV", "IX", "XL", "XC", "CD", "CM"]
        answer = [4, 9, 40, 90, 400, 900]
        for i in range(len(roman)):
            self.assertEquals(answer[i], self.converter.convert(roman[i]), "failed on " + roman[i])

    def test_birthday(self):
        self.assertEquals(1967, self.converter.convert("MCMLXVII"))

    def test_four_ones(self):
        self.assertEquals(4, self.converter.convert("IIII"))

    def test_many_x(self):
        self.assertEqual(100, self.converter.convert("XXXXXXXXXX"))