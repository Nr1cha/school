import pytest
from pytest import approx

def testp():
    p = 6.03
    assert p == approx(6.03)

pytest.main(["-v", "--tb=line", "-rN", __file__])