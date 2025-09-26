def num():
    n = int(input('n = '))
    x = 0
    while n != 0:
        x += n%10
        n = n // 10
    print(x)

num()