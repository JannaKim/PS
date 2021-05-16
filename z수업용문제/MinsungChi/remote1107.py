a= int(input())
b=int(input())
if b==0:
    if len(str(a))>abs(a-100):
        print(abs(a-100))
    else: 
        print(len(str(a))) 

else:
    c=(input())
    c= c.split(' ')
    if b==10:
        print(abs(a-100))
        exit()
    L=[]
    for i in range(0,1000000):
        for j in range(0,len(str(i))):
            if str(i)[j] in c:
                i=-1
                break
        if i==-1:
            continue
        L.append(abs(i-a)+len(str(i)))
    if min(L)>abs(a-100):
        print(abs(a-100))
    else: 
        print(min(L))
