n=int(input())
Gyosu=[]
sunggyu=[]
C= []

for i in range (n):
    a=input().split()
    C.append(a)

#y좌표는C[y]번 좌표는 C[y][x] 
for i in range (n):
    for q in range (n):
        if C[i][q] == "5":
           Gyosu.append(i)
           Gyosu.append(q)
        if C[i][q] == "2":
            sunggyu.append(i)
            sunggyu.append(q)
ST=0
x1=Gyosu[1]
x2=sunggyu[1]
y1=Gyosu[0]
y2=sunggyu[0]



w=abs(x1-x2)
h=abs(y1-y2)

dist=(w**2)+(h**2)

w += 1
h += 1
sx=min(x1,x2)
sy=min(y1,y2)
#검사 시작지는 (min(x1,x2),max(y1,y2))

for i in range (sy,sy+h):#0~2
    for j in range (sx,sx+w):#1~6
        if '1' == C[i][j]:
            ST+=1
    

if dist >= 25:

    if ST >=3:
        print(1)
    else:
        print(0)
else:
    print(0)

'''

7
0 0 0 0 0 2 5
0 0 1 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 1 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

7
2 0 0 0 0 0 0
0 0 0 0 1 0 0
0 0 0 0 1 0 0
0 0 0 0 1 0 0
0 0 0 0 5 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

'''