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

firstoperand=0
while len(expression)>0 and ord(expression[0])>45:
        firstoperand= firstoperand*10+int(expression.pop(0))
expression.insert(0,str(firstoperand))

n= len(expression)
i=1
#print(expression)
while True:
    if i>=n-1: break
    if ord(expression[i])<=45 and expression[i+1]=='0':
        expression.pop(i+1)
        n-=1
        i-=1
    i+=1


#print(''.join(expression))
print(eval(''.join(expression)))
    

# 105+51

# 0005+ 1005+ 05