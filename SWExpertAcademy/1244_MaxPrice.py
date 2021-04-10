for t in range(1,int(input())+1):
    num, k= input().split()
    k=int(k)
    num=list(num)
    n= len(num)
    mx_val= int(''.join(sorted(list(num),reverse=True)))
    
    chk= {}
    mx=[-1,1]
    def backtrack(cnt,num):
        global mx, mx_val, n;
        ans= int(''.join(num))
        if ans==mx_val: #
            if mx[0]<ans:
                mx= [ans,cnt]
            else:
                if mx[1]%2:
                    mx= [ans,cnt]
        if not cnt: #
            if ans==mx[0]:
                mx[1]= cnt
            elif ans>mx[0]:
                mx= [ans, cnt]
            return True
        for i in range(n):
            for j in range(i+1,n):
                nxt= num[:]
                nxt[i], nxt[j]= nxt[j], nxt[i]
                new= int(''.join(nxt))
                if new>=ans and (new,cnt-1) not in chk:
                    chk[(new,cnt-1)]=1
                    backtrack(cnt-1, nxt)
    
    backtrack(k, num)

    print(f'#{t}',end=' ')
    if mx[1]%2:
        a= mx[0]//100*100
        b= mx[0]%100//10
        c= mx[0]%10*10
        print(a+b+c)
    else:
        print(mx[0])

    '''
    1 2 3 4 5 6
    6 2 3 4 5 1
    6 5 3 4 2 1
    6 5 4 3 2 1
    77732 10
    '''

    


'''
473266 3
463267
763264
766234
164376
764316 3

'''



'''
for t in range(1,int(input())+1):
    num, k= input().split()
    k=int(k)
    L=[]
    for idx, el in enumerate(num):
        L.append((el,idx))
    M=L[:]
    L.sort()

    if list(num)==sorted(num,reverse=True):
        ans=sorted(num,reverse=True)
        if not k%2:
            print(''.join(ans))
        else:
            ans[-1], ans[-2]= ans[-2], ans[-1]
            print(''.join(ans))
        continue
    top=len(num)-1
    left=0
    right=top
    ans=[0]*(top+1)
    ls=[]
    chk=[False]*(top+1)
    while left<=right and k:
        if chk[L[right][1]]==True:
            right-=1
            continue
        if chk[M[left][1]]==True or M[left][0]==L[right][0] :
            left+=1
            continue

        k-=1
        if left==right:
            ls.append(M[left][0])
            chk[M[left][1]]=True
            k+=1
        else:
            ls.append(M[left][0])
            ls.append(L[right][0])
            chk[L[right][1]]=True
            chk[M[left][1]]=True
        left+=1
        right-=1
    
    ls.sort()
    #print(ls)
    #print(chk)
    #print(k)
    print(f'#{t}',end=' ')
    for i in range(top+1):
        if chk[i]:
            ans[i]=ls.pop()
        else:
            ans[i]=num[i]
    if not k%2:
        print(''.join(ans))
    else:
        ans[-1], ans[-2]= ans[-2], ans[-1]
        print(''.join(ans))
    




72713
77213
77312
77321
'''