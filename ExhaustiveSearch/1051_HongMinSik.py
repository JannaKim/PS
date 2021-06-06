N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input())))

len = N - 1 if N <= M else M - 1
area = 0

if len == 0:
    area = 1

while(len > 0):
    for i in range(N - len):
        for j in range(M - len):
            if(arr[i][j] == arr[i][j + len] and arr[i][j] == arr[i + len][j] and arr[i][j] == arr[i + len][j + len]):
                area = (len+1) ** 2 if (len+1) ** 2 > area else area
    len -= 1

print(area)