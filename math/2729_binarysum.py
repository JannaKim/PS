import sys; input= lambda: sys.stdin.readline().rstrip(); r= range
for _ in r(int(input())):
    a, b= input().split()
    if int(a)+int(b)==0:
        print(0)
        continue
    a= a[::-1]
    b= b[::-1]
    lenA= len(a)
    lenB= len(b)
    tot=0
    if lenA> lenB:
        b= b+ '0'*(lenA-lenB)
        tot=lenA
    if lenB>= lenA:
        a= a+ '0'*(lenB-lenA)
        tot=lenB
    c=0
    ans=[]
    for op1, op2 in zip(a, b):
        if op1=='1' and op2=='1':
            ans.append(0+c)
            c=1
        elif int(op1)+int(op2)==0:
            ans.append(0+c)
            c=0
        else:
            if 1+c==2:
                ans.append(0)
            else:
                ans.append(1)
                c=0
    erase= True
    if len(ans)==1: erase= False
    if c==1:
        print(1,end='')
        erase= False
    for i in range(tot-1, -1, -1):
        if erase:
            if ans[i]==0: continue
            erase= False
        print(ans[i],end='')
    print()