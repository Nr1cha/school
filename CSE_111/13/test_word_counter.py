from word_counter import read_ext_file, user_input
from pytest import approx
import pytest

def test_read_ext_file():

    variable = read_ext_file()

    assert isinstance(variable, "words2.txt")