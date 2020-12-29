n=int(input())


for i in range (0,n):
    a=[int(i) for i in input().split()]
    b=sorted(a[1:])
    av=float(sum(b)/len(b))
    #print("av=",av)
    for i in range(0,len(b)):
        if float(b[i])>av:
            #print("av=",av,b[i:],len(b))
            print('%.3f' % (len(b[i:])/(len(b))*100),'%',sep='')
            break
