def fizzbuzz(n: int) -> list[str]:
    lst = []
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            lst.append('FizzBuzz')
        elif x % 3 == 0:
            lst.append('Fizz')
        elif x % 5 == 0:
            lst.append('Buzz')
        else:
            lst.append(str(x))
    return lst

    # return ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz'
    #         if x % 3 == 0 else 'Buzz'
    #         if x % 5 == 0 else str(x)
    #         for x in range(1, n + 1)]


if __name__ == '__main__':
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(15))

    assert fizzbuzz(3) == ["1", "2", "Fizz"]
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                            "FizzBuzz"]
