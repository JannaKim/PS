s= input()

case1=0
isOne=False
for el in s:
    if not isOne:
        if el=='1':
            case1+=1
            isOne=True
    
    else:
        if el=='0':
            isOne=False

case2=0
isZero=False
for el in s:
    if not isZero:
        if el=='0':
            case2+=1
            isZero=True
    
    else:
        if el=='1':
            isZero=False
print(min(case1,case2))
