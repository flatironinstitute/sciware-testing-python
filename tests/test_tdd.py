import pytest
import sciware_testing_python

@pytest.mark.skip(reason="not yet implemented")
def test_count_ones():
    assert sciware_testing_python.count_ones([2,1,1,3,-1]) == 2
