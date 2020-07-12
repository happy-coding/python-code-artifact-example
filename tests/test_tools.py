from rare.tools import is_palindrome


def test_is_palindrome():
    assert is_palindrome(None) is False
    assert is_palindrome('rare') is False
    assert is_palindrome('anna') is True
