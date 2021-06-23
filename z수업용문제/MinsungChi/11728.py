a=input()
L=[]
a= a.split(' ')
for i in range(0,2):
    b= input().split(' ')
    for k in range(0,len(b)):
        L.append(int(b[k]))
L.sort()
print(*L)


'ab'
'b'
'a'

# a ab b