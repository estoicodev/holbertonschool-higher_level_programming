#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    s = roman_string
    if s is not None or isinstance(s, str):
        for i in range(len(s)):
            if s[i] == "I":
                if i < len(s) - 1:
                    if s[i + 1] == "V" or s[i + 1] == "X":
                        num -= 1
                    else:
                        num += 1
                else:
                    num += 1
            elif s[i] == "V":
                num += 5
            elif s[i] == "X":
                if i < len(s) - 1:
                    if s[i + 1] == "L" or s[i + 1] == "C":
                        num -= 10
                    else:
                        num += 10
                else:
                    num += 10
            elif s[i] == "L":
                num += 50
            elif s[i] == "C":
                num += 100
            elif s[i] == "D":
                num += 500

    return num
