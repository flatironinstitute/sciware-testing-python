# -*- coding: utf-8 -*-
"""Main module template with example functions."""
from typing import List


def sum_numbers(number_list: List[float]) -> float:
    """Example function. Sums a list of numbers using a for loop.

    Parameters
    ----------
    number_list : list
        List of ints or floats

    Returns
    -------
    int or float
        Sum of list

    Notes
    -----
    This is NOT good Python, just an example function for tests.

    Example
    -------
    >>> 1
    1
    """

    sum_val: float = 0
    for n in number_list:
        sum_val += n

    return sum_val


def add_vectors(vector_1: List[float], vector_2: List[float]) -> List[float]:
    """Example function. Sums the same index elements of two list of numbers.

    Parameters
    ----------
    v1 : list
        List of ints or floats

    v2 : list
        List of ints or floats

    Returns
    -------
    list
        Sum of lists

    Notes
    -----
    This is NOT good Python, just an example function for tests.

    """
    sum_vec = []

    for a, b in zip(vector_1, vector_2):
        sum_vec.append(a * b)

    return sum_vec
