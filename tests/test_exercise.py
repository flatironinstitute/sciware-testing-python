import pytest
from sciware_testing_python import sum_numbers
from sciware_testing_python import add_vectors

def test_sum_numbers_123():
    # basic test to see if we get the expected answer for a simple case.
    sum = sum_numbers([1,2,3])
    assert sum == 6

def test_sum_numbers_yours():
    # write another test of the sum_numbers function
    pass

def test_sum_numbers_empty():
    # what's the sum of an empty list
    pass

# Write a test for the add_vectors function

# Write a test for sum_numbers on a list of booleans

# def test_sum_bools():
#   sum = sum_numbers(["1", "2", "3"])
