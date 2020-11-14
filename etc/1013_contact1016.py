'''
N = int(input('state num: '))
Q=[]
for i in range(N):
    Q.append(tuple([int(j) for j in input(f'Q[{i}]: ').split()]))

print(Q)
'''

T = int(input())
Q = [(0, 0), (8, 2), (3, 0), (4, 0), (4, 5), (8, 6), (7, 6), (4, 9), (0, 9), (8, 2)]
for _ in range(T):  
    cur=1
    for bit in input():
        cur = Q[cur][int(bit)]
    if cur==5 or cur== 6 or cur==9:
        print('YES')

    else:
        print('NO')

'''
3
10010111
011000100110001
0110001011001
'''

