# 재고가 2개 이상 남았을 때만 배송한다?
def solution(n, delivery):

    stock = ['?']*(n+1)
    for row in delivery:
        if row[2]==1:
            if ord(stock[row[0]])<63: # 숫자가 적혀있다면
                stock[int(stock[row[0]])]='X'
            stock[row[0]]='O'
            if ord(stock[row[1]])<63:
                stock[int(stock[row[1]])]='X'
            stock[row[1]]='O'
        else:
            if stock[row[0]]=='X' or stock[row[1]]=='X':
                continue
            if stock[row[0]]=='O' and stock[row[1]]!='O':
                stock[row[1]]='X'
            elif stock[row[0]]!='O' and stock[row[1]]=='O':
                stock[row[0]]='X'
            else: # 둘중 하나가 만드시 x
                stock[row[0]] = str(row[1])
                stock[row[1]] = str(row[0])
    for i in range(1,len(stock)):
        if ord(stock[i])<63: # 아직 숫자가 들어있다면
            stock[i]='?'



    answer = ''.join(stock[1:])
    return answer

d = [[1,3,1], [3,5,0], [5,4,0], [2,5,0]]
d = [[5,6,0], [1,3,1], [1,5,0], [7,6,0], [3,7,1], [2,5,0]]
d = [[1,3,0], [3,5,0], [1,5,0]]
n = 5
print(solution(n,d))

'''
1 3 0
3 5 0
5 7 0
7 9 0
9 11 0
일 때 적어도 세 개 이상은 확실히 X
'''