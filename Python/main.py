def func(a, b):
    if b == 1:
        return 0
    x = 1
    r = 0
    while True:
        r = a * x - (x - 1)
        if r >= b:
            return x
        x = x + 1


if __name__ == '__main__':
    a,b = [int(x) for x in input().split()]
    print(func(a,b))