for _ in range(int(input())):
    s= input()
    lo=0
    hi=len(s)-1
    def rec(left, right, s):
        mid= (left+right)//2
        if mid==left:
            return True
        if s[left]==s[right]:
            return False
        if rec(left,mid-1,s) and rec(mid+1,right,s):
            return True
        else:
            return False
    if rec(lo,hi,s):
        print('YES')
    else:
        print('NO')

