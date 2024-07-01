def three_consecutive_odds(arr: list[int]) -> bool:
    c = 0
    for n in arr:
        c = c + 1 if n % 2 != 0 else 0
        if c == 3:
            return True
    return False


if __name__ == '__main__':
    assert three_consecutive_odds([2, 6, 4, 1]) is False
    assert three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 17]) is True
