x=list(input())

for i in range (len(x)):
    x[i]=int(x[i])
if 0 not in x:
    print(-1)
    exit()
x=sorted(x)[::-1]
if sum(x)%3==0:
    for el in x:
        print(el, end='')
else:
    print(-1)



#80875542
