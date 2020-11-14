T = int(input())

for _ in range(T):
    wv = input()
    Q = [(7,1), (2,9), (3,9), (3,4), (7,5), (6,5), (3,8), (9,8), (7,1), (9,9)]
    n=0
    for bit in wv:
        n = Q[n][int(bit)]
    if n==4 or n==5 or n==8:
        print('YES')
    else:
        print('NO')

'''
3
10010111
011000100110001
0110001011001
'''