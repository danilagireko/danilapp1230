def a():
    a = int(input('число 1:'))
    b = int(input('число 2:'))
    c = int(input('число 3:'))
    d = b**2- 4*a*c
    if d > 0:
      print(f'x1 = {-b+(d**0.5)//2*a}')
      print(f'x2 = {-b-(d**0.5)//2*a}')
    elif d == 0:
      print(f'x = {-b//2*a}')
    else:
      print('нет корней')

a()

           # print(math.sqrt(c))
           # print(c* 0.5)