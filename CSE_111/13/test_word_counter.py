from fileinput import filename
from word_counter import all_text_to_lower, read_ext_file, get_word_occurances, clean_file
# from pytest import approx
import pytest

def test_read_ext_file():
    file = read_ext_file("words.txt")
    print(file)
    assert isinstance(file, str)

def test_get_word_occurances():
    user_word = "the"
    file_contents = "the brown fox jumped over the log"
    output = get_word_occurances(user_word, file_contents)
    assert output[0] == 2

def test_clean_file():
    output = clean_file("the file? is ,here.")
    assert output == "the file is here"

def test_all_text_to_lower():
    output = all_text_to_lower("The file Is Lowercase")
    assert output == "the file is lowercase"

pytest.main(["-v", "--tb=line", "-rN", __file__])