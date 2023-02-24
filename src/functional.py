def primeNumbersFunc(num: int) -> int:
    a = 0
    b = 1
    counter = 0
    while counter != (num - 1):
        counter += 1
        if counter % 2 == 0:
            a += b
            c = a
        else:
            b += a
            c = b
    return c
