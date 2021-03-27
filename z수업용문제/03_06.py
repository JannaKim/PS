def f(n):
    print(n)
    for i in range(n-1,-1,-1):
        print(f'f({i})')
        f(i)
f(5)