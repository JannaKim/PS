n= int(input())
n-=1


def rec(i,s):
    #print(i,s)
    global n
    if i==n+1:
        print(''.join([str(el) for el in s]))
        exit()

    i+=1
    for tst in range(1,4):
        if len(s)!=0 and s[-1]==tst:
            continue
        s.append(tst)

        flag=True
        for gap in range(1,(n+1)//2+1): 
            if i-2*gap>=0 and s[i-gap:i]==s[i-2*gap:i-gap]:
                flag=False
                break
            #print(f'{s}, s[{i-gap}:{i}], s[{i-2*gap}:{i-gap}]')
        if flag:
            rec(i,s)

        s.pop()

    



rec(0,[])