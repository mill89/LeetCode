def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    n_arr = []
    for n in nums1:
        if n in nums2:
            n_arr.append(nums2.pop(nums2.index(n)))
    return n_arr


assert intersect([1, 2, 2, 1], [2]) == [2]
assert intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]

print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
