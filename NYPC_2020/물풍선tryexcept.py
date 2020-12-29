a = int(input())

L = []
for i in range(a):
    L.append([0] * a)


for i in range(a):
    b = [int(i) for i in input().split()]
    L[b[0]-1][b[1]-1] = 1

ans = {}

for i in range(a-2):
    X = i+1
    for j in range(a-2):
        Y = j+1

        if L[X][Y] == 1:
            ke = str(X+1)+' '+str(Y+1)
            try:
                n = 1
                piv = L[X-n][Y]*L[X][Y]*L[X+n][Y]*L[X][Y-n]*L[X][Y+n]
                while piv == 1:
                    ans[ke] = n
                    n += 1
                    piv = L[X-n][Y]*L[X][Y]*L[X+n][Y]*L[X][Y-n]*L[X][Y+n]
            except:
                pass

if len(ans) == 0:
    print('-1')
else:
    print(len(ans))
    for k, v in ans.items():
        print(k+' '+str(v))
