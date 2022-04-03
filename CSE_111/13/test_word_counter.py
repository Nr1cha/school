from word_counter import read_ext_file, get_word_occurances, clean_file, all_text_to_lower
from pytest import approx
import pytest

def test_read_ext_file():

    variable = read_ext_file()

    assert isinstance(variable, "words.txt")



def test_user_input():

    print()

def test_clean_file():

    print()

def test_all_text_to_lower():

    print()

pytest.main(["-v", "--tb=line", "-rN", __file__])