def sum():
    k = int(input('k='))
    n = int(input('n='))
    x = 0
    for i in range(k, n+1):
        if i % 2 != 0:
            x += i
    print(x)

sum()