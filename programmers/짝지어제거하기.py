def solution(s):
    stc=[]
    top=-1
    for el in s:
        if el==top:
            stc.pop()
            if stc:
                top=stc[-1]
            else:
                top=-1
        else:
            top=el
            stc.append(el)
    if not stc:
        return 1
    else:
        return 0

print(solution('baabaa'))