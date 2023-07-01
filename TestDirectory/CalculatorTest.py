import pytest

from TestDirectory.Calculator import *

@pytest.mark.parametrize("a,b,expected_result",[(10,2,5),(20,10,2)])
def test_division_good(a,b,expected_result):
    assert division(a,b) == expected_result

