import pytest
from sciware_testing_python import count_ones_kc

# @pytest.mark.skip(reason="not yet implemented")
def test_count_ones():
    assert count_ones_kc([2,1,1,3,-1]) == 2

