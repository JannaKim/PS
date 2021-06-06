P = []
ans=0
for i in range ( 9 ):
    a = int( input() )
    P.append( [a , i+1] )
P.sort()
print(*(P[-1]), sep= '\n') 

#print(*P[-1]) # , sep = '\n')

#print(1,2,3 , end= 'a')

