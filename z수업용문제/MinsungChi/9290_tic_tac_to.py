n=int(input())
L=[]
for k in range(0,n):
    for j in range(0,3):
        w= input()
        L.append(list(w))
        xo=input()
def check (a, b, c , xo):
    a.split(' ')
    o=0
    
    if L[a // 3][a % 3]==xo:
        o+=1
    if L[b // 3][b % 3]==xo:
        o+=1
    if L[c // 3][c % 3]==xo:
        o+=1
    
    if o==2:
        return True
    else:
        return False

t1= check(1, 2, 3)
t2= check(4, 5, 6)
t3= check(7, 8, 9)
t4= check(1, 4, 7)
t5= check(2, 5, 8)
t6= check(3, 6, 9)
t7= check(3, 5, 7)
t8= check(1, 5, 9)

