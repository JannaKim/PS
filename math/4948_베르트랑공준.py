m = 123456
M = 2 * m
prime = [True] * (M + 1)
prime[0] , prime[1] = False , False

for i in range(2, int(M ** (0.5)) + 1):
    if prime[i]:
        for j in range(2*i , M + 1, i):
            prime[j] = False


while True:
    n = int(input())
    if not n:
        break
    lo = n + 1
    hi = n * 2
    ans = sum([1 if prime[i] else 0 for i in range(lo , hi + 1)])
    print(ans)