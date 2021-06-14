n= int(input())
for i in range(0,n):
    c= (input())
    b= (input())
    a=0
    for e , k in zip(c , b):
        if e[j]!=k[j]:
        a+=1
        print(f'Hamming distance is {a}.')
    
    '''
    for j in range(0,len(c)):
        if c[j]!=b[j]:
            a+=1
    print(f'Hamming distance is {a}.')
'''


