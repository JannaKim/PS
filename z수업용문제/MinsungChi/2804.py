a = input()
a = a.split()

w1 = a[0]
w2 = a[1]
L=[]
for g in range(0, len(w2)):
    L.append(['.']*len(w1))




def fill(k, i):
    for d in range(0,len(w1)):
        L[k][d] = w1[d]
    for h in range(0, len(w2)):
        L[h][i] = w2[h]

flag = False

for i in range(0, len(w1)):
    for k in range(0, len(w2)):
        if w1[i]==w2[k]:
            L[k][i]=w1[i]
            # cheugi fill
            fill(k, i)
            flag = True
            break
    if flag==True:
        break   


for j in range(0, len(w2)):
    print (*L[j], sep = '')
