import text_parser.parser as script


##############################################
################## PARSER ####################
##############################################

def test_remove_uppercase():
    p = script.Parser("BonJouR")
    p.remove_uppercase()
    assert p.user_text == "bonjour"


def test_remove_special_char():
    p = script.Parser("ÀÆŒÇÈÌÐÑÒŠÙÝ¢")
    p.remove_special_char()
    assert p.user_text == "aaeoeceidnosuyoe"


def test_remove_double_space():
    p = script.Parser("Bonjour  Bonjour")
    p.remove_double_space()
    assert p.user_text == "Bonjour Bonjour"


def test_remove_stopwords():
    p = script.Parser("bonjour je suis grandpy le papybot")
    p.remove_stopwords()
    assert p.user_text == "papybot"


def test_call_all_methods():
    p = script.Parser("Bonjour  Bonjour ÓÓÓÓÓÓ ailleurs")
    p.call_all_methods()
    assert p.user_text == "oooooo"
