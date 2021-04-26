t=int(input())
m=0
while t!=-0:
    for i in range (7):
        a= 2**(6-i)
        if t<a:
            continue
        else:
            m+=1
            t=t-a

print(m)