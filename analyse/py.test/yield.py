# Aufruf mit py.test -q -s <dateiname>
import pytest

@pytest.fixture
def setup_teardown():
    print ("setup")
    yield 1
    print ("\nteardown")

def test_setup_teardown(setup_teardown):
    assert setup_teardown == 1
