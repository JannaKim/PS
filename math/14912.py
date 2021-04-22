n, d= input().split()
d=int(d)

digits= len(n)
N= len(n)
s=0
realnum= int(n)

if d!=0:
    for digit, el in enumerate(n):
        if digit==0:
            if int(el)>d:
                if digit+1<N-1:
                    s+=10**len(n[digit+1:])

            elif int(el)==d:
                if digit+1<=N-1:#
                    s+=int(n[digit+1:])+1
                else:
                    s+=1
        else:
            front= int(n[:digit])
            back=0
            backLen= 0
            if digit+1<=N-1:
                back= int(n[digit+1:])
                backLen= 10**len(n[digit+1:])
            if int(el)<d:
                if digit+1<=N-1:
                    s+= front*backLen
                else:
                    s+= front
            elif int(el)==d:
                if digit+1<=N-1:
                    s+=front*backLen
                    s+=back+1
                else:
                    s+=front+1
            
            else:
                if digit+1<=N-1:
                    s+= (front+1)*backLen
                else:
                    s+= front+1

   

else:
    for i in range(1,realnum+1):
        nm=i
        while nm>0:
            if nm%10==d:
                s+=1
            nm//=10
print(s)
            


