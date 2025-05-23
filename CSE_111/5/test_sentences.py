from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

# from words import prefix, suffix
# def main():


def test_get_determiner():
    # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():  # TODO
    # 1. Test the single noun.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural determiners.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns


def test_get_verb():  # TODO
    # 1. Test the single verb past.

    single_verb_past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, "past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_verb_past

    # 2. Test the plural present plural.

    verb_present_plural = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(1, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in verb_present_plural

    verb_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walks", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(0, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in verb_present

    verb_future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep",
                "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(0, "future")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in verb_future



def test_get_preposition():
    preposition_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    split_word = get_preposition().split(' ')

    word = split_word[0]

    assert word in preposition_words

def test_get_prepositional_phrase(): 
    preposition_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    single_determiners = ["a", "one", "the"] 
    plural_determiners = ["two", "some", "many", "the"]


    split_word = get_prepositional_phrase(1).split(' ')

    preposition = split_word[0]
    determiner =  split_word[1]
    noun =  split_word[2]

    assert preposition in preposition_words
    assert determiner in single_determiners
    assert noun in single_nouns


    split_word = get_prepositional_phrase(0).split(' ')

    preposition = split_word[0]
    determiner =  split_word[1]
    noun =  split_word[2]

    assert preposition in preposition_words
    assert determiner in plural_determiners
    assert noun in plural_nouns

    # single_prepositions = get_prepositional_phrase(1)
    # for _ in range(4):
    #     word = get_preposition(1)
    #     assert word in single_prepositions

    # plural_prepositions = get_prepositional_phrase(0)
    # for _ in range(4):
    #     word = get_preposition(0)
    #     assert word in plural_prepositions

pytest.main(["-v", "--tb=line", "-rN", __file__])
