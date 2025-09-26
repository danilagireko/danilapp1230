def ap():
    n = int(input('кол-во школьников'))
    k = int(input('кол-во яблок'))
    print(f'остаток:{k%n}')
    print(f'каждому по:{k//n}')

ap()
