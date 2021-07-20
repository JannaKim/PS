L = list(map(int, input().split(' ')))#input 받는거 list로 넣기

a, b, c = map(int, input().split(' '))

L = []

L=[0]*5

for k in range(0, 10):
    L.append([0]*11)

H=[]
for k in range(0, 10):#중간에 1로 채우기
    H.append([0]*11)
for i in range(2, 2+6):
    for j in range(3, 3+4):
        H[i][j]= '1'

for k in range(0,10):
    print(*H[k])


L = []                  #max쓰지 않고 최대값 구하기
for i in range(0, 9):
    i = int(input())
    L.append(i)
mx = 0
idx = 0
for i in range(0, len(L)):
    if L[i] > mx:
        mx = L[i]
        idx = i + 1
print(mx)
print(idx)


L = []

for _ in range(4):
    L.append([0] * 4)

for i in range(4):         #   삼각형으로 출력
    for j in range(0, i-1):
        L[i][j] = 1

for s in range(0,a):        # *사용할때 공백 없애기
    print(*L[s], sep = '')

L=[]                        
a= int(input())
for k in range(0, a):
    L.append([' ']*a)
    
for i in range(a):
    for j in range(a - 1 - i, a):
        
        L[i][j] = '*'

for s in range(0,a):
    print(*L[s], sep = '')
#   *
#  **
# ***