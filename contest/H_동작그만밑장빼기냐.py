N = int(input())
L = [int(i) for i in input().split()]
F=[]
even=[0]*(N+1)
even[0]=L[0]
for i in range(2,N,2):
    even[i]=even[i-2]+L[i]

_from = [0]*(N+1)
_from[N-1]=L[-1]
for i in range(N-3,-1,-2): # 밑장빼서 주고 i번째부터 홀수번쨰 카드 모았을 시
    _from[i]=_from[i+2]+L[i]


mx = sum([L[i] for i in range(0,N,2)])
for i in range(0,N,2):
    if L[i]<L[i+1]:
        mx=max(mx, (even[i-2] if i-2>=0 else 0) + (_from[i+1] if i+1<N else 0))

print(mx)


'''
6
3 2 5 2 1 3
'''