n = int(input())
I = []

ans=0
for i in range (n):
    t=input()
    I.append(t)
for i in I:
    if len (i)==1:
        ans+=1
    else:
    
        a=0
        H = [False] * 26
        for q in range (len(i)):
            
            if H[ ord( i[q] )-97 ]==False:
                H[ ord( i[q] )-97 ]=True
                a+=1
                #print(i , q , H[ ord( i[q] ) -97 ], a )
            
            elif H[ ord( i[q] )-97 ] == True:
                if i[ q ] != i[ q-1 ]:
                    a += 0
                else:
                    a+=1
                print(len(i),a)
        if a == len( i ):
            ans += 1
print(ans)