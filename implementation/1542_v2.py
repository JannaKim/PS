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
n= len(q)
i=0
while True:
    if i==n-1: break
    if q[i]=='0' and ord(q[i+1])>45:
        q.pop(i)
        n-=1
        i-=1
    i+=1

#print(''.join(q))
print(eval(''.join(q)))



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