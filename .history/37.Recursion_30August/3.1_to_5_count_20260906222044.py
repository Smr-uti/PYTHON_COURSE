def count_up(n, limit):
    if n > limit:
        return n
    print(n)
    return count_up(n + 1, limit)

result = count_up(1, 5)