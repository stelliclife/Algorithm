def get_knapsack(capacity, items):
    table = []
    result = []
    n, c = 0, 0
    while n <= len(items):
        if c > capacity:
            table.append(result)
            result = []
            c = 0
            n += 1
        if c == 0 or n == 0:
            result.append(0)
            c += 1
            continue
        w = items[n-1][0]
        if w > c:
            result.append(table[n-1][c])
            c += 1
            continue
        value = items[n-1][1] + table[n-1][c-w]
        if value <= table[n-1][c]:
            result.append(table[n-1][c])
        else:
            result.append(value)
        c += 1

    return table[-1][-1]