N, M = map(int, input().split())
X = []
Y = []
for _ in range(M):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
if M%2: #홀수
    _x = X[M//2]
    _y = Y[M//2]
else: #짝수
    _x = (X[M//2-1]+X[M//2])//2
    _y = (Y[M//2-1]+Y[M//2])//2

summ = 0
for i in X:
    summ += abs(_x-i)
for i in Y:
    summ += abs(_y-i)

print(summ)

'''
4 4
1 2
1 4
3 1
4 2
'''