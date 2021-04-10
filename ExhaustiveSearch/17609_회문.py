import sys; input= lambda: sys.stdin.readline().rstrip()
t= int(input())
for _ in range(t):
    s= input()
    left=0
    right= len(s)-1
    flag=False
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
            continue
        if s[left+1]==s[right] and s[left]==s[right-1]:
            tst= s[left+1:right+1]
            if tst==tst[::-1]:
                print(1)
                flag=True
                break
            tst=s[left:right]
            if tst==s[left:right][::-1]:
                print(1)
                flag=True
                break
        elif s[left+1]==s[right]:
            tst=s[left+1:right+1]
            if tst==tst[::-1]:
                flag=True
                print(1)
                break
            else:
                flag=True
                print(2)
                break
        elif s[left]==s[right-1]:
            tst=s[left:right]
            if tst==tst[::-1]:
                flag=True
                print(1)
                break
            else:
                flag=True
                print(2)
                break
        else:
            flag=True
            print(2)
            break
    if not flag:
        print(0)
