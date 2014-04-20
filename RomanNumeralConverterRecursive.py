

__author__ = 'phred'


class RomanNumeralConverterRecursive:

    def convert_roman(self, roman):
        if roman.count == 0:
            return 0
        elif roman == "I":
            return 1
        elif roman == "V":
            return 5
        elif roman == "X":
            return 10
        else:
            return self.convert_roman(roman[0]) + self.convert_roman(roman[1:])
