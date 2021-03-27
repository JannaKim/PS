#print(ord('1'), ord('9'),ord('a')-87, ord('z'))
import sys; input= lambda: sys.stdin.readline().rstrip()
MAX=2**63
#print(2**63)
def conversion(ths, to):
    s=0
    for idx, digit in enumerate(ths[::-1]):
        cur=0
        if ord(digit)<97: # realnum
            cur=int(digit)
        else:
            cur=ord(digit)-87
        if cur>=to:
            #print(cur,to)
            return 1e20
        #print(f'{cur}*({to}**{idx})= {cur*(to**idx)}')
        s+=cur*(to**idx)
    return s


#print(conversion('ep',13))
#print(conversion('jh',10))

ans=-1
a=0
b=0
A, B= input().split()
for i in range(2,37):
    for j in range(2,37):
        if i==j:
            continue
        res1= conversion(A,i)
        res2= conversion(B,j)
        if res1>=MAX or res2>=MAX:
            continue
        if res1==res2:
            #print(res1, i, j, ans)
            if ans>=0:
                print('Multiple')
                exit()
            ans=res1
            a,b=i,j
if ans<0:
    print('Impossible')
    exit()
print(ans,a,b)

