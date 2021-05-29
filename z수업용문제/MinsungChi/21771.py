a= input()
a= a.split(' ')
L=[]
b= input()
b= b.split(' ')
for w in range(0,int(a[0])):
    c= input()
    L.append(c)
an=0
for k in range(0, int(a[0])):
    for l in range(0,int(a[1])):
        if L[k][l]=='P':
            an+=1
if int(b[2])* int(b[3])>an:
    print(1)
else:
    print(0)