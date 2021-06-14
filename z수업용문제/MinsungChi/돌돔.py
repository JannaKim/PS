a= input()
a= a.split(' ')
d=[]
s=''
b, c = '', ''
for i in range(0,int(a[0]) ):
    b+=input()

for i in range(0,int(a[0]) ):
    c+=input()

for k in range(0,int(a[1])* int(a[0])):    
    s=s+b[k]*2

if c==s:
    print('Eyfa')
elif c!=s:
    print('Not Eyfa')
'''
2 2
AB
CD
AAB
BCCDD
'''