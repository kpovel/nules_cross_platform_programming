def fib(n):
    if (n == 0 or n == 1):
        return n

    return fib(n - 1) + fib(n - 2)


def fib_list(k):
    if (k == 0):
        return [0]

    list = fib_list(k - 1)
    list.append(fib(k))
    return list


print(fib_list(10))
