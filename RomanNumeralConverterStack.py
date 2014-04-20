__author__ = 'phred'


class RomanNumeralConvertStack:

    def convert(self, roman):
        numerals_map = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
                        "CM": 900,
                        "M": 1000}

        the_answer = 0
        index = 0
        while index < len(roman):
            two_char = roman[index:index + 2]
            if two_char in numerals_map:
                the_answer += numerals_map[two_char]
                index += 2
            else:
                the_answer += numerals_map[roman[index]]
                index += 1

        return the_answer