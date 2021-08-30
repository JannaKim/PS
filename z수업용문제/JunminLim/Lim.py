
P = {}
P[key]=value

if key in P:



L = list(map(int, input().split())) # 한줄을 int형 리스트로

L = list(map(str, input().split())) 

a, b = list(map(int, input().split()))

a, b, c = [1, 2, 3]

g = (g + 1) % 3

x1 y1 x2 y2

y,x 구하기: min(y1,y2)
h,w       min(x1,x2)
         abs(y1-y2)
         abs(x-x2)   


root(a)<=x == a <= x**2  
Q=[]
for i in range (9):
    Q.append([0]*9)
for i in range (y,y+h):
    for j in range (x, x+w):
        Q[i][j]=1

a-=1
b-=1
x1,y1=a//4,a%4
x2,y2=b//4,b%4

ans = abs(x1-x2)+abs(y1-y2)
print(ans)

def f(x):
    return x + 1

1 2 3   0,0 0,1 0,2
4 5 6   1,0 1,1, 1,2
7 8 9 ==2,0 2,1 2,2  L[a//3][a%3]==L[1~9]
sort하고 싶으면 A.sort()
sort 전 후가 필요하면 sorted(A)


'''

-------
0 1 2 3
-------
4 5 6 7    - >   가로길이를 이용.
-------     y = 숫자 //  가로길이    6=(1,2)
8 9 . .     x = 숫자 % 가로길이       =(6//4,6%4)
 1,2 ---> 1X4 +2 = 6
 1,3 ---> 1X4 +3
 2, 1 --->2X4+1

y, x를 안다면 몇 번?

가로길이 X 숫자


'''