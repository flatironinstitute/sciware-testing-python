# -*- coding: utf-8 -*-
"""Tests for `sciware_testing_python` package."""

import random
import pytest
import sciware_testing_python as stp


def test_sum_numbers():
    """Sample test function for sum_numbers."""

    assert 0 == stp.sum_numbers([])

    number_list = [2, 3, 4]
    our_result = stp.sum_numbers(number_list)
    assert our_result == sum(number_list)


def test_adding_vectors():
    v1 = [2, 0]
    v2 = [2, 0]
    assert stp.add_vectors(v1, v2) == [4, 0]


def test_add_zero_length_vectors():
    """ Test function for adding empty vectors"""
    assert stp.add_vectors([], []) == []


#######################################################################
#                        Advance pytest topics                        #
#######################################################################
# Pytest useful decorators
# - fixture
# - mark.xfail
# - mark.parametrize
# - mark.skip

# Possible other discussion
# - pytest.approx(val, rel=1e-5)


@pytest.fixture
def generate_numbers():
    """Sample pytest fixture. Generates list of random integers.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

    return random.sample(range(100), 10)

#######################################################################


def test_random_sum_numbers(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = stp.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers)


@pytest.mark.xfail
def test_random_sum_numbers_add_1(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = stp.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers) + 1


@pytest.mark.xfail
def test_sum_numbers_with_bad_args():
    """ Test sum numbers when not given good input
    """
    bad_number_list = ['these', 'R', False, "#s"]
    result = stp.sum_numbers(bad_number_list)


@pytest.mark.parametrize("number_list,  expect_val", [
    ([1, 2, 3], 6),
    ([-2, 0, 1], -1),
    ([3.5, 7.25, -.75], 10),
])
def test_parametrize_sum_numbers(number_list, expect_val):
    assert stp.sum_numbers(number_list) == expect_val


@pytest.mark.xfail
def test_add_different_length_vectors():
    """
    """
    v1 = [2, 3, 4]
    v2 = [4, 9, 16, 25]
    result = stp.add_vectors(v1, v2)  # doctest: +IGNORE_EXCEPTION_DETAIL


@pytest.mark.skip
def test_add_skip_test():
    """ This test would fail if not for the decorator
    """
    assert False
