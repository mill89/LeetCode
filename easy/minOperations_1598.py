def min_operations(logs: list[str]) -> int:
    count = 0
    for i in logs:
        if i == '../':
            count = count - 1 if count > 0 else count
        elif i == './':
            continue
        else:
            count += 1
    return count


assert min_operations(["d1/", "d2/", "../", "d21/", "./"]) == 2
assert min_operations(["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3
assert min_operations(["d1/", "../", "../", "../"]) == 0
