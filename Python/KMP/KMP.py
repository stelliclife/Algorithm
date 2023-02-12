def get_pattern_size(keyword):
    k, count = 1, 0
    data = []
    for i in range(1, len(keyword) + 1):
        target = keyword[:i]
        if len(target) < 2:
            count = 0
        else:
            if target[:k] == target[-k:]:
                count += 1
                k += 1
            else:
                k, count = 1, 0
        data.append(count)
    return max(data)


def run_kmp(keyword, target):
    start, matched, n = 0, 0, 0
    pattern_size = get_pattern_size(keyword)
    m, result = 0, 0

    while (n+len(keyword)) < len(target):
        if keyword[:m] == target[n:n+m]:
            m += 1
        else:
            m -= 1
            if m == 0:
                n += 1
            elif m == len(keyword):
                result = n
                n = n + m - pattern_size
            else:
                n += m
            m = 0
    return result