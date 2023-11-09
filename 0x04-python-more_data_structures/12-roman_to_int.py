#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    else:
        result = 0
        value_befor = 0
        numR = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for char in reversed(roman_string):
            value_reversed = numR.get(char, 0)
            if value_reversed < value_befor:
                result -= value_reversed
            else:
                result += value_reversed
            value_befor = value_reversed
        return result
