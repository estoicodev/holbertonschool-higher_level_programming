#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = []
    for i in range(len(my_list)):
        if my_list[i] != search:
            new.append(my_list[i])
        else:
            new.append(replace)

    return new
