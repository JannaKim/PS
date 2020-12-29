import copy

a, b = [int(i) for i in input().split()]
maaaap = input()
L = []

for i in range(a): # a가 세로
    L.append([0]*b)


   
C = copy.deepcopy(L)

for i in range(a): # L안에 지도의 내용물을 넣어주고
    mapp = input()
    for j in range(b):
        if (mapp[j] == 'L'):
            L[i][j] = 1 # 1을 땅으로
        elif (mapp[j] == 'S'):
            L[i][j] = 2 # 2 바다
        else:
            L[i][j] = -1 # 물음표







answer=0
if(maaaap=='min'):
   
    #print(L)
    for i in range(a): # 현재 좌표가 물음표라면, 주변에 땅이 하나라도 있으면 주변 물음 표 다 땅으로 채우기
        for j in range(b):
            if L[i][j]==-1:
                # L[0][0] ~ L[a-1][b-1]
                # b가 j고 가로
                
                if j+1<=b-1 and L[i][j+1]==1:
                    L[i][j]=1
                    
                elif 0<= j-1 and L[i][j-1]==1:
                    L[i][j]=1
                    
                elif 0<=i-1 and L[i-1][j]==1:
                    L[i][j]=1
                    
                elif i+1<=a-1 and L[i+1][j]==1 :
                    L[i][j]=1
                    
                else: 
                    L[i][j]=2
                    print(i,j,"바다칠했다")
                   
 
               
    #print(L)            
               
else: #max
    for i in range(a): #현재 좌표가 땅일때, 오른쪽이나 아래가 물음표면 바다로 채우기
        for j in range(b):
            if L[i][j] == 1: # L[0][0] ~ L[a-1][b-1] i+1<=a-1   i
                if i+1<=a-1 and L[i+1][j]!=1:
                    L[i+1][j] = 2
                if j+1<=b-1 and L[i][j+1]!=1: # j+1<=b-1
                    L[i][j+1] = 2 #오른쪽이랑 아래 바다로 채우기
                   
               
    for i in range(a): # 나머지 빈칸을 땅물땅물로 바꾸는 전략인데, 이렇게 하면 반례그림에서 걸린다.
        for j in range(b):
            if L[i][j]==-1:
                L[i][j]=1 

                if i+1<=a-1 and L[i+1][j]==-1:
                    L[i+1][j]=2
                if j+1<=b-1 and L[i][j+1]==-1:
                    L[i][j+1]=2 
                   



z=0    


#print(C)

for i in range(a): # 세는게 완벽하지않앗다
        for j in range(b):
            if L[i][j] == 1: # 4 5 L[3][4]
                if C[i][j]!=3: # 확인되지 않은 땅을 체크했을떄 꼬리에 꼬리를 물고 체크해주자
                    z += 1
                    C[i][j] = 3
                    #print("여기가 새 땅이라서 땅 셌다.",i,j,C[i][j])

                
                if C[i][j]==3:
                    #print(i,j)
                    if i+1<=a-1: # 아래가 존
                        if L[i+1][j] == 1 and C[i+1][j]!=3: #아래가땅이었다
                            C[i+1][j] = 3
                            y=0 # 아래 i+1<=a-1
                            
                            while (1):
                                if i+1+y <=a-1 and L[i+1+y][j]==1:
                                    
                                    C[i+1+y][j] = 3 # L 좌우대칭으로 이어진 땅 찾자
                                    #print("L자 찾기",i+1+y,j)
                                    
                                else:
                                    break
                                x=0 
                                while (1):
                                    if j-x >=0 and L[i+1+y][j-x]==1:
                                        
                                        C[i+1+y][j-x]=3
                                        #print("L자 찾기",i+1+y,j-x)
                                        x+=1
                                    else:
                                        break
                                y+=1
                           
                    if j+1<=b-1:
                        if L[i][j+1] == 1:
                            C[i][j+1] = 3

                            
                           
#print(C)                
                   

                            
print(z)



