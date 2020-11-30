T = int(input())
for _ in range(T):
    *L,= map(int, input().split())
    av=sum(L[1:])/L[0]
    s=sum([1 for el in L[1:] if el>av])
    print(f'{s/L[0]*100:0.3f}%')