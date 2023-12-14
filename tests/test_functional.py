from webapp.vsearch import search4letters


def test_search4letters():
    phrase = 'this is just a test'
    letters = 'aeiou1'
    results = search4letters(phrase=phrase, letters=letters)
    assert results == {'i', 'a', 'u', 'e'}
