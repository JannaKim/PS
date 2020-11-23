# (100~1~ | 01)~
Q = ( (0,0), (7,2), (3,0), (4,0), (4,5), (7,6), (8,6), (0,1), (4,1) )

S = input()
idx = 1
for el in S:
    idx = Q[idx][int(el)]

if idx ==1 or idx == 5 or idx == 6 or idx == 8:
    print('SUBMARINE')
else:
    print('NOISE')
