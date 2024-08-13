def roman_to_int(s: str) -> int:
    ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = ROMAN[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total



if __name__ == '__main__':
    print(roman_to_int("MCMXCIV"))
    print(roman_to_int("LVIII"))

    # assert roman_to_int("III") == 3
    # assert roman_to_int("LVIII") == 58
    # assert roman_to_int("MCMXCIV") == 1994
