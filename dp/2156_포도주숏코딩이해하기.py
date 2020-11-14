N = int(input())
a,b,c = 0,0,0
for _ in range(N):
    num = int(input())
    a, b, c = max(c, b), max(a + num, b), max(b + num, c)
    #a, b, c = max(a,b,c), a + num, b + num
print(max(a, b, c))

'''
6
6
10
13
9
8
1

6
6       
0 6 6   
10      
6 10 16 
13      
16 19 23
9       
23 25 28
8       
28 31 33
1       
33 31 33
33    
'''