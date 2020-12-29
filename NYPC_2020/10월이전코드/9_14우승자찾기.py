N=int(input())
K =int(input())
A = [0]*(K+1) # C에선 A(N+1, 0)

# A[0], += 쓰거나 A[1:] 하거나
A[1:] = [int(i) for i in input().split()]
#A = list(map(int, input().split()))

ans = []
for i in range(1, N+1):
    recent = [0] * (N+1)
    chk = False
    for j in range(1,K+1):
        if A[j] != i and recent[A[j]] >= recent[i]:
            chk = True
        recent[A[j]] = j
        if A[j] == i:
            if not chk:
                ans.append(i)
                break
            chk = False


print(len(ans))
#for it in ans:
    #print(it, end=' ')
   
print(' '.join(list(map(str, ans))))



# [a for a in list123 if lambda a: fdjas]
