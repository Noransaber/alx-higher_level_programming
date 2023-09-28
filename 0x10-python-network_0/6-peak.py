#!/usr/bin/python3
"""FINDS THE PEAK"""


def find_peak(list_of_integers):
    """FIND THE PEAK """

    if list_of_integers is None or list_of_integers == []:
        return None
    low = 0
    hight = len(list_of_integers)
    mid = ((hight - low) // 2) + low
    mid = int(mid)
    if hight == 1:
        return list_of_integers[0]
    if hight == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
