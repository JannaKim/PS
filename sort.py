L= [5,2,6,1,2,6,2,8]
# radix 정수, 양수여야함
# 1억까진 됨, 커지면 정렬안됨
def QS(A, first, last):
    # 0~3에서 정렬이안됐다
    print(f'first, {first}, last, {last}')
    if first>=last:
        return
    p = A[first]
    left = first+1 # 피봇보다 작은것
    right = last # 피봇보다 크거나 같은것
    while left<right:
        while A[left]<=p and left<=last: # 피봇보다 작으면 넘어감
            left+=1
        # 하면 left는 p보다 큰 애에서 멈춤
        while A[right]>p and first<=right: # 피봇보다 크거나 같으면 넘어감
            right-=1
        #스왑
        if left<=right:
            A[left], A[right] = A[right], A[left]
            left +=1
            right -=1

    # 뒤집어졌을때 피봇이랑 R이랑 스왑
    if first<right:
        print('정렬')
        A[first], A[right] = A[right], A[first]

    # 피봇을 기준으로 왼쪽은 피봇보다 작, 오른쪽은 큼
    print(A)
    QS(A, first, right-1)

    QS(A, left, last)


QS(L, 0,len(L)-1)
print(L)