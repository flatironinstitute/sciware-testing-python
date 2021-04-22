# -*- coding: utf-8 -*-
"""Tests for `sciware_testing_python` package."""

import random

import pytest

import sciware_testing_python as stp
# import sciware_testing_python_sol as stps


def test_sum_numbers():
    """Sample test function for sum_numbers."""

    number_list = [2, 3, 4]
    our_result = stp.sum_numbers(number_list)
    assert our_result == sum(number_list)


def test_adding_vectors():
    v1 = [2, 3, 4]
    v2 = [4, 9, 16]
    assert stp.add_vectors(v1, v2) == [6, 12, 20]


def test_add_zero_length_vectors():
    """ """
    assert stp.add_vectors([], []) == []


############################################################
# Pytest useful decorators
# - fixture
# - mark.skip
# - mark.parametrize
# - mark.xfail


@pytest.fixture
def generate_numbers():
    """Sample pytest fixture. Generates list of random integers.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

    return random.sample(range(100), 10)


skip = pytest.mark.skip
parametrize = pytest.mark.parametrize
xfail = pytest.mark.xfail
###########################################################


def test_random_sum_numbers(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = stp.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers)


@pytest.mark.xfail
def test_random_sum_numbers_add_1(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = stp.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers) + 1


@xfail(strict=True)
def test_add_different_length_vectors():
    """TODO: Docstring for test_add_zero_length_vectors.
    @return: TODO

    """
    assert False


@skip
def test_add_skip_test():
    """TODO: Docstring for test_add_zero_length_vectors.
    @return: TODO

    """
    assert False


@xfail
def test_adding_vectores_with_bad_args():
    """TODO: Docstring for test_adding_lists_with_bad_args.
    @return: TODO

    """
    assert False
# TEST_CASE("Test Adding Vectors with Bad Args")
# {
#     // Setup
#     const int N = 10, M = 100;
#     std::vector<double> v1(N);
#     std::vector<double> v2(M);

#     // Generally check that it throws an exception
#     REQUIRE_THROWS(add_vectors(v1, v2));

#     // Check that it throws a specific type of exception
#     REQUIRE_THROWS_AS(add_vectors(v1, v2), std::invalid_argument);
# }
    pass
