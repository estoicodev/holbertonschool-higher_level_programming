#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str

    cpy_p1 = str[0:n]
    cpy_p2 = str[n+1:]
    cpy = cpy_p1 + cpy_p2
    return cpy
