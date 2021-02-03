import sys; input= lambda: sys.stdin.readline().rstrip()
s= input()

operate=False
q= []
a=''
b=0
for el in s:
    if not operate:
        if el!='+':
            q.append(el)
        else:
            while q and q[-1]!='-':
                #print(q[-1])
                a=q.pop()+a
            #print('a',a)
            operate=True
    else:
        if ord(el)>45:
            b=10*b+int(el)
        elif el=='-':
            q.append(str(int(a)+b))
            q.append('-')
            a=''
            b=0
            operate=False
        else:
            a=str(int(a)+b)
            b=0
#print(a,b)
if a:
    q.append(str(int(a)+b))

#print(q)


i=1
corner=0
while len(q)>0 and len(q[0])==1 and ord(q[0])>45:
    corner= 10*corner+ int(q.pop(0))
if corner: # 처음에 스트링이었으면 코너가 필요없었음
    q.insert(0,str(corner))
n= len(q)
#print(q)
while True:
    if i>=n-1: break # 여기 조심. 첫길이 1이었을대 생각.
    if len(q[i])==1 and ord(q[i])<=45 and q[i+1]=='0':
        q.pop(i+1)
        n-=1
        i-=1
    i+=1

#print(''.join(q))
print(eval(''.join(q)))

#반례: 105+51-105
# 10+100-05

'''


10-1-3+5

1


55-50-40+40-50
-125


05+060
65


55-50+40+30
120


4-3+6-7-9
-21
'''