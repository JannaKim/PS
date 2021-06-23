n= input()
L=[]
for i in range(0, len(n)):
    if (ord(n[i])-65)//3==0:
        L.append(3)
    elif (ord(n[i])-65)//3==1:
        L.append(4)
    elif (ord(n[i])-65)//3==2:
        L.append(5)
    elif (ord(n[i])-65)//3==3:
        L.append(6)
    elif (ord(n[i])-65)//3==4:
        L.append(7)
    
    elif 15 <= (ord(n[i])-65) <= 18:
        L.append(8)
    elif 19<=(ord(n[i])-65)<=21:
        L.append(9)
    elif  22 <=(ord(n[i])-65) <= 25:
        L.append(10)
a=0
for k in range(0,len(L)):
    a=a+L[k]
print (a)