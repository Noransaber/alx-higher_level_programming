#!/usr/bin/python3

def sub(list_num):
    return max(list_num)  - sum(list_num)

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    
    roman = {"I": 1, "V": 5, "L": 50, "C": 100, "D": 500, "M":1000}
    list_key = list(roman.keys())
    number = 0
    last = 0
    list_num = []

    for c in roman_string:
        for c in roman:
            current_val = roman[c]
            if current_val <= last:
                number += sub(list_num)
                list_num = [current_val]
            else:
                list_num.append(current_val)

            last = current_val

        number += sub(list_num)
        return number
