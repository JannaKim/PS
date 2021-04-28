import sys; input= lambda:sys.stdin.readline().rstrip()
def chk(s,switch):
    rev=s[::-1]
    if rev==s:
        if not switch:
            return 0
        else:
            return 1
    else:
        if not switch:
            n= len(s)
            tmp=2
            for i in range(n):
                if rev[i]!=s[i]:
                    tmp= min(tmp,chk(s[:i]+s[i+1:], True))
                    tmp= min(tmp,chk(s[:n-i-1]+s[n-i:], True))
                    return tmp
        else:
            return 2
        
for _ in range(int(input())):
    s= input()
    print(chk(s,False))
