start = int(input("Enter Start: "))
end = int(input("Enter End: "))

if start > end:
    start, end = end, start


def is_prime(n, end):
    if n == end:
        return True

    if end % n == 0:
        return False
    else:
        return is_prime(n + 1, end)


def rec_is_prime(i, end):
    if i > end:
        return

    if is_prime(2, i):
        print(i, "is prime")
    else:
        print(i, "isn't prime")

    rec_is_prime(i + 1, end)


rec_is_prime(start, end)
