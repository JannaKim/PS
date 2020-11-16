N = int(input())
L = [int(i) for i in input().split()]
L.sort(reverse=True)

mx= bin(L[0])[2:]
rv_mx = [str((int(i)^1)) for i in mx]
rv_mx=''.join(rv_mx)
print(rv_mx)
ans=L[0]
print(int(rv_mx,2), 2**(len(mx)-1))
for i in range(int(rv_mx,2), 2**(len(mx)-1)):
    if i in L:
        print(bin(i)[2:])
        ans = ans+i
        break
print(str(ans)*2)
