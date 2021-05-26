a= (input())
a= a.split(' ')
dic={}
for i in range(1,int(a[0])+1):
    b= (input())
    dic[b]=i
    dic[str(i)]=b 

    
for h in range(0,int(a[1])):
    c= (input())
    print(dic[c])
    
