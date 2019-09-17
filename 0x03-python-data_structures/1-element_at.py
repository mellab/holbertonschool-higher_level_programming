#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)

    elements = len(my_list)

    if idx > elements - 1:
        return (None)

    return(my_list[idx])
