for _ in range(int(input())):
    s= input()
    n= len(s)
    ans=[]
    m= int(input())
    if '*' not in s:
        for _ in range(m):
            ths=input()
            if len(ths)!=n:
                continue
            flag=True
            for a, b in zip(s, ths):
                if a=='?':
                    continue
                if a!=b:
                    flag=False
                    break
            if flag:
                ans.append(ths)
    else:

        left= s.index('*')
        hi=s[::-1].index('*')

        right= n-1-hi
        print(left,right)
        for _ in range(m):
            ths=input()
            ori=ths[:]
            thsLen= len(ths)
            thsright= thsLen-1-hi

            flag=True
            if (left!=0 and ths[:left]!=s[:left]) or (right!= n-1 and ths[thsright:]!=s[right:]):
                flag=False
            else:
                ths=ths[left:thsright+1]
                print(ths)
                s= s[left+1:right]
                s= ''.join(s.split('*'))
                print('별뺌',s)
                end= len(s)
                thsLen= len(ths)
                up=0
                down=0
                while up<end:
                    if s[up]=='?':
                        up+=1
                        down+=1
                        if down==thsLen and up!=end:
                            flag=False
                            break
                    while s[up]!=ths[down]:
                        down+=1
                        if down==end:
                            flag=False
                            break
                    up+=1

            if flag:
                ans.append(ori)
    [print(el) for el in sorted(ans)]


'''
https://github.com/Jim741305/osfall2020
'''