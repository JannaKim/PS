n=int(input())

found=0
for i in range (0,n):
    a=[int(i) for i in input().split()]
    b=sorted(a[1:])
    #print(b)
    av=float(sum(b)/a[0])
    #print("av=",av)
    for i in range(0,len(b)):
        if float(b[i])>av:
            found=1
            #print("av=",av,b[i:],len(b))
            #print((len(b[i:])/(len(b))*100))
            print('%.3f' % (len(b[i:])/(a[0])*100),'%',sep='')
            break
    if(found==0):
        print("0.000%")
