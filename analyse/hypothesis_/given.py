from hypothesis import given
from hypothesis.strategies import integers


@given(integers())
def test_int(i):
    assert (i + i) == (i * 2)


if __name__ == '__main__':
    test_int()
