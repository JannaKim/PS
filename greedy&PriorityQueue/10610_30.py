n= input()
isZero=False
q=[]
for el in n:
    if el=='0' and not isZero:
        isZero=True
    else:
        q.append(int(el))
q.sort(reverse=True)
if isZero and not sum(q)%3:
    [print(el,end='') for el in q]
    print(0)
else:
    print(-1)
