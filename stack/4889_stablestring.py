idx=0
while True:
    idx+=1
    s=input()
    if s[0]=='-':
        break

    q=[]
    top=-1
    for el in s:
        if el=='}' and top>=0 and q[top]=='{':
            q.pop()
            top-=1
        else:
            top+=1
            q.append(el)

    Len= len(q)
    #print(Len)
    if not Len:
        print(f'{idx}. 0')
    else:
        ans=0
        for i in range(0,Len,2):
            if q[i]!='{':
                ans+=1
            if q[i+1]!='}':
                ans+=1
        print(f'{idx}. {ans}')

