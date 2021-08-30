n=int( input())
an=[]
L=[]
for k in range(0, n):
    a= input()
    L.append(a)
for el in (list(zip(*L))):
    el= set(el) 


    if len(el)==1:
        an= an+ list(el)
    else:
        an= an +['?']
        

for s in range(0,1):        # *사용할때 공백 없애기
    print(*an, sep = '')

