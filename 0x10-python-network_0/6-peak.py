#!/usr/bin/python3

"""
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if not list_of_integers:
        return None
    return fp(list_of_integers, 0, len(list_of_integers) - 1,
              len(list_of_integers))


def fp(arr, low, high, n):
    """Helper func"""
    mid = low + (high - low)//2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and\
       (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return fp(arr, low, mid - 1, n)
    else:
        return fp(arr, mid + 1, high, n)
