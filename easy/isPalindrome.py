def is_palindrome(x: int) -> bool:
    x = str(x)
    return x == x[::-1]


if __name__ == '__main__':
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
