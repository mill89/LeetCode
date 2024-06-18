def middleNode(head):
    return head[len(head) // 2:]


if __name__ == '__main__':
    print(middleNode([1, 2, 3, 4, 5]))
    print(middleNode([1, 2, 3, 4, 5, 6, 3, 6, 9, 5, 4, 1, 9]))

    assert middleNode([1, 2, 3, 4, 5]) == [3, 4, 5]
    assert middleNode([1, 2, 3, 4, 5, 6]) == [4, 5, 6]
