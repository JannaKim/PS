from math import log


def catch_digit(num, d):
    return (num//10**d)%10


def radix(A,d):
    k=9
    B= [-1]*len(A)
    C= [0]*(k+1)

    #현재 자릿수를 기준으로 빈도수 세기
    for a in A:
        C[catch_digit(a, d)] +=1
    #C업데이트
    print('C',C)
    for i in range(k): #??????????
        C[i+1]+=C[i]
    print('C update',C)
    # 현재 자릿수를 기준으로 정렬
    for j in reversed(range(len(A))):
        print(j)
        B[C[catch_digit(A[j], d)]-1]= A[j]
        print(f'B[C[catch_digit({A[j]}, {d})]-1]= {A[j]}')
        print(f'B[C[{catch_digit(A[j], d)}]-1]= A[j]')
        print(f'B[{C[catch_digit(A[j], d)]}-1]= A[j]')
        print(f'{B[C[catch_digit(A[j], d)]-1]}= A[j]')
        C[catch_digit(A[j], d)]-=1
    print('   B', B)
    return B




def radix_sort(L):
    # 받은 리스트 요소중 최대 자릿수 확인   
    digit = int(log(max(L),10))
    #자릿수별로 counting sort
    for d in range(digit+1):
        ans=radix(L,d)
    return ans

L = [3,1,4,1,5,9,2,6,5]
print(radix_sort(L))

print([[0]*10 for _ in range(8)])