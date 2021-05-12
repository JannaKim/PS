def solution(places):
    ans=[]
    for room in places:

        flag=False
        for i in range(5):
            for j in range(4):

                if room[i][j]=='P' and room[i][j+1]=='P':
                    flag=True
                    
                    break
                if room[j][i]=='P' and room[j+1][i]=='P':

                    flag=True
                    break
        for i in range(3):
            for j in range(3):

                if room[i][j]=='P' and room[i][j+1]=='O' and room[i][j+2]=='P' :
                    flag=True
                    
                    break
                if room[i][j]=='P' and room[i+1][j]=='O' and room[i+2][j]=='P' :
                    flag=True
                    break
        for i in range(4):
            for j in range(4):
                if room[i][j]=='P' and room[i][j+1]=='O' and room[i+1][j+1]=='P':

                    flag=True
                    break
                if room[i][j]=='O' and room[i][j+1]=='P' and room[i+1][j]=='P':

                    flag=True
                    break
                if room[i][j]=='P' and room[i+1][j]=='O' and room[i+1][j+1]=='P':
                    #print(i,j)
                    flag=True
                    break
                if room[i][j+1]=='P' and room[i+1][j]=='P' and room[i+1][j+1]=='O':
                    #print(i,j)
                    flag=True
                    break
        if flag:
            ans.append(0)
        else:
            ans.append(1)
    return ans

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXPP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))