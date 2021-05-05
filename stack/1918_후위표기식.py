import sys; sys.setrecursionlimit(100000)
s= input()
n= len(s)


def cal(lo,hi):
    if lo>hi:
        return ''
    if s[lo]=='(':
        for i in range(lo+1,hi+1):
            if s[i]==')':
                if i+1<n:
                    ths=s[i+1]
                    return cal(lo,i)+ths+cal(i+2,hi)
    if s[lo]=='+':
        if s[lo+1]=='(':
            tmp=''
            for i in range(lo+2,hi+1):
                if s[i]==')':
                    tmp+= cal(i,hi)+'+'
                
                    return tmp+cal(i+1,hi)
        else:
            return cal(lo+1,hi)+'+'
    if s[lo]=='*':
        if s[lo+1]=='(':
            tmp=''
            for i in range(lo+2,hi+1):
                if s[i]==')':
                    tmp+= cal(lo+2,i-1)+'*'
                
                    return tmp+cal(i+1,hi)
        else:
            return s[lo+1]+'*'+cal(lo+2,hi)
    else:
        return s[lo]+cal(lo+1,hi)


print(cal(0,n-1))
