import sys; input= lambda: sys.stdin.readline().rstrip()
s= input()

expression= []
start=True
flag=False
for el in s:
    if el=='-':
        if start:
            expression.append(el)
            expression.append('(')
            start=False
            flag=True
        else:
            expression.append(')')
            expression.append(el)
            expression.append('(')
            flag=True
    else:
        expression.append(el)
if flag:
    expression.append(')')


# erase invalid zero
n= len(expression)
i=0
while True:
    if i==n-1: break
    if expression[i]=='0' and ord(expression[i+1])>45:
        expression.pop(i)
        n-=1
        i-=1
    i+=1

print(''.join(expression))
print(eval(''.join(expression)))
    