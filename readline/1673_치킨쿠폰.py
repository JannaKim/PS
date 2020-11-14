import sys
f = sys.stdin
while True:
    input = f.readline()
    if not input: break
    a, b = map(int,input.split())
    s = a
    while a//b>=1:
        chicken = a//b
        s +=chicken
        a = a-chicken*b+chicken
        
    print(s)

'''
4 3
10 3
100 5
'''