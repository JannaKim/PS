T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    a=N%H
    if not a:
        a=str(H)
    else:
        a=str(a)

    b= N//H+1
    if not N%H:
        b-=1
    b=str(b)
    if len(b)==1:
        b='0'+b
    
    print(a+b)

'''
2
6 12 10
30 50 72
'''