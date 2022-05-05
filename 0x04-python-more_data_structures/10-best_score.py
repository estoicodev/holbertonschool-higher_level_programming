#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    max = 0
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            max_key = key

    return max_key
