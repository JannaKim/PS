t, p = map(int, input().split())
used=100-p
if p<20:
    used+=20-p
#print(used)
permin= used/t
#print(permin)
ans=permin*p
ans+=min(p,20)*permin
print(ans)


if p>=20:
    permin= (100-p)/t
    print((p+20)*permin)
else:
    used=100-p+20-p
    permin= used/t
    print(p*permin*2)