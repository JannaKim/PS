a= int(input())
L=[]
L = list(map(int, input().split(' ')))
f=0
an=0
for k in range(0, int(a)):
    if L[k]==f:
        an= an+1
        '''
        f=f+1
        if f==3:
            f=0
        '''
        f = (f + 1) % 3
        
print(an)
