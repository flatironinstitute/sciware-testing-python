import pytest
import sciware_testing_python

def test_sum1():
    # basic sanity test: do we get the right answer for a simple case?
    assert True #sciware_testing_python.sum_numbers([1,2,3]) == ?

def test_sum2():
    # what's the sum of an empty list
    pass

#@pytest.mark.xfail(strict=True, raises=TypeError)
def test_sum_bools():
    pass
