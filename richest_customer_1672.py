def maximum_wealth(accounts: list[list[int]]) -> int:
    return max(sum(n) for n in accounts)


if __name__ == '__main__':
    print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))  # 6
    print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))  # 10
