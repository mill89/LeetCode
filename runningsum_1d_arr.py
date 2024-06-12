# Input: nums = [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
def running_sum(nums: list[int]) -> list[int]:
    return [sum(nums[:n + 1]) for n in range(len(nums))]


if __name__ == '__main__':
    print(running_sum([1, 2, 3, 4]))
