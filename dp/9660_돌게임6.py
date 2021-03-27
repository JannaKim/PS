# 1 3 2 6 4 5
'''
n= input()[::-1]

rule= (1,3,2,6,4,5)
one=0
for idx, num in enumerate(n):
    one+=int(num)*rule[idx%6]



ls= [*map(int, list(n))]
#print(ls)
carry=0
if int(ls[0])>=5:
    carry=1
ls[0]=(ls[0]+5)%10
if carry:
    for idx, num in enumerate(ls[1:]):
        ls[idx+1]=(ls[idx+1]+carry)%10
        if not ls[idx+1]:
            break

two=0
for idx, num in enumerate(ls):
    two+=num*rule[idx%6]

if not one%7 or not two%7:
    print('CY')
else:
    print('SK')
'''
import sys; input= lambda: sys.stdin.readline().rstrip(); e=enumerate
n= input()[::-1]

rule= (1,3,2,6,4,5)
one=0
for idx, num in e(n):
    one+=int(num)*rule[idx%6]

ls= [*map(int, list(n))]

c=0
if int(ls[0])>=5:
    c=1
ls[0]=(ls[0]+5)%10
if c:
    for idx, num in e(ls[1:]):
        tmp=(ls[idx+1]+c)%10
        if ls[idx+1]>tmp:
            ls[idx+1]=tmp
        else:
            ls[idx+1]=tmp
            break
two=0
for idx, num in e(ls):
    two+=num*rule[idx%6]

if not one%7 or not two%7:
    print('CY')
else:
    print('SK')



