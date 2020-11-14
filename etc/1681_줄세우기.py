N, L = map(int, input().split())
L=str(L)
i=0
cnt=0
while cnt<N:
    i+=1
    if L not in str(i):
        cnt+=1
print(i)
