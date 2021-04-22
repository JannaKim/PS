t, p = map(int, input().split())
if p>=20:
    
    permin= (100-p)/t
    print((p+20)/permin)
else:
    used=100-p+20-p
    permin= used/t
    print(p*2/permin)


'''
1: x% = 120: 120%
'''