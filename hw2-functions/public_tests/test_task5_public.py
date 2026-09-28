import pytest
from task5 import memoize

pytestmark = pytest.mark.bonus


def test_memoize_returns_same_result():
    @memoize
    def square(x):
        return x * x

    assert square(5) == 25
    assert square(5) == 25
