from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    ransom_count = Counter(ransom_note)
    magazine_count = Counter(magazine)

    # Проверяем, хватает ли букв из magazine для составления ransomNote
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True




if __name__ == '__main__':
    print(can_construct('al', 'milan'))

    assert can_construct('al', 'milan') is True
    assert can_construct('nad', 'sakfjdhfjdskfk') is False
    assert can_construct('null', 'ndugelal') is True
