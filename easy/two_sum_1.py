def two_sum(nums: list[int], target: int) -> list[int]:
    num_to_index = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in num_to_index:
            return [num_to_index[diff], index]
        num_to_index[num] = index


if __name__ == '__main__':
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
