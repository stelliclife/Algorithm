MEMO = [0, 1]


def fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursion(n-2)+fibonacci_recursion(n-1)


def fibonacci_memoization(n):
    global MEMO

    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n >= len(MEMO):
        value = fibonacci_memoization(n-2) + fibonacci_memoization(n-1)
        MEMO.append(value)
    return MEMO[n]