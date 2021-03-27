# 그때받은걸로 별로 다 차 있는 종이만든다

# 

def recursion(y, x, Len):
    if Len==1:
        return
    byThird= Len//3

    recursion(y, x, byThird)
    recursion(y, x+byThird, byThird)
    recursion(y, x+2*byThird, byThird)
    recursion(y+byThird, x, byThird)
    #빈칸 채우기 여기 채우기
    recursion(y, x, byThird) # 여기 시작좌표 조정하기
    recursion(y, x, byThird)
    recursion(y, x, byThird)
    recursion(y, x, byThird)

