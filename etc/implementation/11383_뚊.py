N, M = map(int, input().split())
a = []
for _ in range(2*N):
    a.append(input())
_not=False
for i in range(N,2*N):
    for j in range(2*M):
        #print(f"{a[i][j]} {a[i%N][j//2]}")
        if a[i][j] != a[i%N][j//2]:
            _not=True
            print("Not Eyfa")
            break
    if _not:
        break

else:
    print("Eyfa")


