def RS(s):
    q=[]
    isR=True
    for el in s:
        if el=='(':
            q.append('(')
        else:
            if q:
                q.pop()
            else:
                isR=False
                break
    if q:
        isR=False
    return isR

def solution(p):

    return do(0,len(p)-1,p)

def findm(lo, hi,p):
    left=0
    right=0
    for i in range(lo,hi+1):
        if p[i]=='(':
            left+=1
        else:
            right+=1
        #print(left*right, left, right,'?')
        if left*right and left==right:
            return i

def do(lo, hi,p):
    #print(lo,hi,p)
    if lo>=hi:
        return ''

    if RS(p[lo:hi+1]):
        return p[lo:hi+1]
    mid=findm(lo,hi,p)
    #print('mid',mid)
    u=p[lo:mid+1]
    #print('u',u, 'v',v)

    if RS(u):
        return u+do(mid+1,hi,p)
    inside= u[1:-1]


    inside=list(inside)
    for i in range(len(inside)):
        if inside[i]=='(':
            inside[i]=')'
        else:
            inside[i]='('

    return '('+do(mid+1,hi,p)+')'+''.join(inside)


#print(solution("(()())()"))
#print(solution(")("))
print(solution("()))((()"))