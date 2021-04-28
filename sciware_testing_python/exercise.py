# -*- coding: utf-8 -*-
"""Main module template with example functions."""


def sum_numbers(number_list):
    """Sums a list of numbers using a for loop.

    Parameters
    ----------
    number_list : list
        List of ints or floats

    Returns
    -------
    int or float
        Sum of list

    Example
    -------
    >>> sum_numbers([1,2,3])
    6

    Add another doctest below
    >>> 1
    1
    """

    sum_val = 0
    for n in number_list:
        sum_val += n

    return sum_val


def add_vectors(vector_1, vector_2):
    """Adds the corresponding elements of two lists of numbers.

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
    """
    add_vec = []

    for a, b in zip(vector_1, vector_2):
        add_vec.append(a * b)

    return add_vec

def count_ones(input_list):
    count = 0
    for n in input_list:
        if n == 1:
            count += 1

    return count

# Make a new function which counts the number of twos in a list
#def count_twos(input_list):
