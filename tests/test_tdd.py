import pytest
from sciware_testing_python import *

def test_count_ones():
    assert count_ones([2,1,1,3,-1]) == 2

@pytest.mark.skip(reason="not yet implemented")
def test_count_twos():
    assert count_twos([2,1,1,3,-1]) == 1
