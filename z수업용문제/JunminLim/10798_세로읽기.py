p=[]
x=[]
for i in range (5):
    a=input()
    p.append(a)
m=-1
for i in range(5):
    m= max(m, len(p[i]))
for i in range (5):
    if len(p[i])<m:
        p[i]= p[i]+' '*(m-len(p[i]))
        
#[print(el+'.') for el in p]
for i in range (m):
    x.append(p[0][i])
    x.append(p[1][i])
    x.append(p[2][i])
    x.append(p[3][i])
    x.append(p[4][i])

tmp= ''.join(x).split(' ')
print(''.join(tmp))


