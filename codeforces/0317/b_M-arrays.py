import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n, m= map(int, input().split())
    L=[*map(int, input().split())]
    if n==1:
        print(1)
        continue
    mul=False
    ans=n
    dic={}
    for el in L:
        ths=el%m
        #print(el,ths)
        if not ths:
            if not mul:
                mul=True
                continue
            ans-=1
            continue
        if ths in dic:
            dic[ths]+=1
        else:
            dic[ths]=1
    chk={}
    half=m//2
    if m%2:
        half+=1
    if not m%2:
        if half in dic:
            ans-=(dic[half]-1)
    A= sorted(dic.keys())
    for el in A:
        #print(ans)
        #print('el',el)
        #print(m-el)
        if el>=half:
            break
        if m-el in dic:
            #print('y')
            a, b= dic[el], dic[m-el]
            if a==b:
                #print(a,b)
                ans-=(2*a-1)
                continue
            if a+b==2:
                ans-=1
                continue
            if a>b:
                a, b= b,a
            ans-=2*a
    print(ans)


            
'''
6 6
1 2 3 4 5 6

6 6
1 1 1 1 1 4

4 6
6 7 8 9

4 1
1 1 1 1

7 5
1 4 2 3 5 5 5
'''