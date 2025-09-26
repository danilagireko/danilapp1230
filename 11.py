def mm():
    n = int(input())
    a = [0] * n
    a1 = set(a)
    while len(a1) !=len(a):
        for i in range(n):
            a[i] = random.randint(1,10)
        print(a)
        m1 = 0
        m2 = 0
        m1_i,m2_i = 0,0
        for i in range(n):
            if a[i] <m1:
                m1 = a[i]
                m1_i = i
            if a[i] >m2:
                m2 = a[i]
                m2_i = 2

mmx()

