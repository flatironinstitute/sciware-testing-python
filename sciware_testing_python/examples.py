# -*- coding: utf-8 -*-
"""Main module template with example functions."""
from typing import List, TypeVar


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

    Examples
    --------
    >>> number_list = [2, 3, 4]
    >>> sum_numbers(number_list)
    9

    Empty lists are returned as zero
    >>> zero_number_list = []
    >>> sum_numbers(zero_number_list)
    0

    Does not sum strings. Will return value error
    >>> not_number_list = [2, 3, 'stuff']
    >>> sum_numbers(not_number_list) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        raise TypeError(
    TypeError: sum_numbers sums a list containing only ints and floats

    Nor will it sum list of lists, dicts, sets, or tuples.
    # doctest: +IGNORE_EXCEPTION_DETAIL
    >>> another_not_number_list = [[4], 5]
    >>> sum_numbers(another_not_number_list)
    Traceback (most recent call last):
        raise TypeError(
    TypeError: ...

    Bools are alright though.
    >>> bool_list = [True, False, False, True, True]
    >>> sum_numbers(bool_list)
    3

    Will sum tuples
    >>> number_tuple = (4, 9, 16)
    >>> sum_numbers(number_tuple)
    29

    """

    sum_val: float = 0
    for n in number_list:
        if not isinstance(n, (float, int)):
            raise TypeError(
                'sum_numbers sums a list containing only ints and floats.')
        sum_val += n

    return sum_val


def add_vectors(vector_1: List[float], vector_2: List[float]) -> List[float]:
    """Example function. Adds the corresponding elements of two lists of numbers.

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

    Examples
    --------
    >>> v1 = [2, 3, 4]
    >>> v2 = [4, 9, 16]
    >>> add_vectors(v1, v2)
    [6, 12, 20]

    Will not sum vectors of different lengths
    >>> v3 = [2, 3, 4]
    >>> v4 = [4, 9, 16, 25]
    >>> add_vectors(v3, v4) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        raise RuntimeError(
    RuntimeError: add_vectors can only add vectors of the same length.

    Adding two empty vectors will also return an empty vector
    Will not sum vectors of different lengths
    >>> v0 = []
    >>> add_vectors(v0, v0) # doctest: +IGNORE_EXCEPTION_DETAIL
    []

    Will only take lists
    >>> t1 = (2, 4, 8)
    >>> t2 = (3, 9, 27)
    >>> add_vectors(t1, t2) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        raise ValueError(
    ValueError: add_vectors can only sum vectors that are lists.

    """
    if not isinstance(vector_1, list) or not isinstance(vector_2, list):
        raise ValueError(
            'add_vectors can only sum vectors that are lists.')

    if len(vector_1) != len(vector_2):
        raise RuntimeError(
            'add_vectors can only add vectors of the same length.')

    add_vec = []
    for a, b in zip(vector_1, vector_2):
        add_vec.append(a + b)

    return add_vec

A = TypeVar('A')
def count_equal(input_list: List[A], target: A) -> int:
    """Example function. Counts the number of target values in a list.

    Parameters
    ----------
    input_list : list
        List of values
    target : any
        Value to search for

    Returns
    -------
    int
        Numbers of values that == target

    Examples
    --------
    >>> count_equal([2,1,1,3,-1], 1)
    2

    Empty lists are returned as zero
    >>> count_equal([], [])
    0

    """

    count = 0
    for n in input_list:
        if n == target:
            count += 1

    return count


def count_ones(input_list: List[float]) -> int:
    return count_equal(input_list, 1)

def count_twos(input_list: List[float]) -> int:
    return count_equal(input_list, 2)
