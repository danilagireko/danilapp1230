def s1():
    s = input('s=')
    a1 = s.find('a')
    a2 = s.rfind('a')
    s1 = s[:a1+1]+s[a2-1:a1:-1]+s[a2:]
    s2 = s[a1+1:]
    a3 = s2.find('a')+ len(s[:a1+1])
    print(s1)
    print(a3)

s1()