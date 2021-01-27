n, d= input().split()
d=int(d)
N= len(n)
num= int(n)
s=0
if d!=0:
    for digit, el in enumerate(n):
        back= num%(max(10**(N-1-digit),1))
        backLen= 1
        front= max(num//(10**(N-digit)),1)

        if digit+1<=N-1:
            backLen= 10**len(n[digit+1:])

        if digit==0:
            if int(el)>d:
                if digit+1<N-1:
                    s+=backLen

            elif int(el)==d:
                if digit+1<=N-1:
                    s+=back+1
                else:
                    s+=1
        else:
            if int(el)<d:
                s+= front*backLen
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
    n=int(n)
    for i in range(1,n+1):
        nm=i
        while nm>0:
            if nm%10==d:
                s+=1
            nm//=10
print(s)
            


