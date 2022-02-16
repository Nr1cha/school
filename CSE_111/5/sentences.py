import random


def main():
    verb_a = get_verb(1, 'past')
    determiner_a = get_determiner(1)
    noun_a = get_noun(1)
    new_prep_a = get_prepositional_phrase(1)
    print(f"{determiner_a} {noun_a} {verb_a} {new_prep_a}")

    verb_b = get_verb(1, 'present')
    determiner_b = get_determiner(1)
    noun_b = get_noun(1)
    new_prep_b = get_prepositional_phrase(1)
    print(f"{determiner_b} {noun_b} {verb_b} {new_prep_b}")

    verb_c = get_verb(1, 'future')
    determiner_c = get_determiner(1)
    noun_c = get_noun(1)
    new_prep_c = get_prepositional_phrase(1)
    print(f"{determiner_c} {noun_c} {verb_c} {new_prep_c}")

    verb_d = get_verb(0, 'past')
    determiner_d = get_determiner(0)
    noun_d = get_noun(0)
    new_prep_d = get_prepositional_phrase(0)
    print(f"{determiner_d} {noun_d} {verb_d} {new_prep_d}")

    verb_e = get_verb(0, 'present')
    determiner_e = get_determiner(0)
    noun_e = get_noun(0)
    new_prep_e = get_prepositional_phrase(0)
    print(f"{determiner_e} {noun_e} {verb_e} {new_prep_e}")

    verb_f = get_verb(0, 'future')
    determiner_f = get_determiner(0)
    noun_f = get_noun(0)
    new_prep_f = get_prepositional_phrase(0)
    print(f"{determiner_f} {noun_f} {verb_f} {new_prep_f}")

    # print(get_prepositional_phrase(0))


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".

    If quantity == 1, this function will return either "a",
    "one", or "the".
    Otherwise, this function will return
    "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise, this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.

    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"

    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        rand_single_noun = random.choice(single_nouns)
        return rand_single_noun
    else:
        plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        rand_plural_noun = random.choice(plural_nouns)
    return rand_plural_noun


def get_verb(quantity, tense):

    # Return a randomly chosen verb.
    # If tense is "past"
    # This function will return one of these ten verbs:
    #     "drank", "ate", "grew", "laughed", "thought",
    #     "ran", "slept", "talked", "walked", "wrote"

    verb_past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # If tense is "present" and quantity is 1
    # This function will return one of these ten verbs:
    #     "drinks", "eats", "grows", "laughs", "thinks",
    #     "runs", "sleeps", "talks", "walks", "writes"

    verb_present_plural = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # If tense is "present" and quantity is NOT 1
    # This function will return one of these ten verbs:
    #     "drink", "eat", "grow", "laugh", "think",
    #     "run", "sleep", "talk", "walk", "write"

    verb_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walks", "write"]

    # If tense is "future"
    # This function will return one of these ten verbs:
    #     "will drink", "will eat", "will grow", "will laugh",
    #     "will think", "will run", "will sleep", "will talk",
    #     "will walk", "will write"

    verb_future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep",
                   "will talk", "will walk", "will write"]

    # Parameters
    #     quantity: an integer that determines if the
    #         returned verb is single or plural.

    #     tense: a string that determines the verb conjugation,
    #         either "past", "present" or "future".
    # Return: a randomly chosen verb.
    if tense == "past":
        rand_past = random.choice(verb_past)
        return rand_past
    elif tense == "present" and quantity == 1:
        rand_present_plural = random.choice(verb_present_plural)
        return rand_present_plural
    elif tense == "present" and quantity != 1:
        rand_present = random.choice(verb_present)
        return rand_present
    elif tense == "future":
        rand_future = random.choice(verb_future)
        return rand_future


def get_preposition():
    # """Return a randomly chosen preposition
    # from this list of prepositions:
    #     "about", "above", "across", "after", "along",
    #     "around", "at", "before", "behind"`, "below",
    #     "beyond", "by", "despite", "except"`, "for",
    #     "from", "in", "into", "near", "of",
    #     "off", "on", "onto", "out", "over",
    #     "past", "to", "under", "with", "without"

    preposition_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # Return: a randomly chosen preposition.
    preposition_word = random.choice(preposition_words)
    return preposition_word



def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.


    Parameter
        quantity: an integer that determines 
        if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

main()
