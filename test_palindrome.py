from main.py import is_palindrome

def test_right_palindrome():
    assert is_palindrome("level") == True
    assert is_palindrome("minim") == True
    assert is_palindrome("rotator") == True

def test_casesensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Aibohphobia") == True

def test_wrong_palindrome():
    assert is_palindrome("Abdul") == False
    assert is_palindrome("Course") == False
    assert is_palindrome("Northeastern") == False