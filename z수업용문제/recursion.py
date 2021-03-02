import sys; sys.setrecursionlimit(10000)

a= '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
b= '"재귀함수가 뭔가요?"'
c= '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
d= '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
e= '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'


def f(x):
    global a,b,c,d,e
    if x==0:
        print('____'*n+ b)
        print('____'*n+ "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print('____'*n+ "라고 답변하였지.")
        return
    print('____'*(n-x)+ b)
    print('____'*(n-x)+ c)
    print('____'*(n-x)+ d)
    print('____'*(n-x)+ e)
    x-=1
    f(x)
    print('____'*(n-x-1)+ '라고 답변하였지.')


n= int(input())
print(a)
f(n)



'''
4 0
3 1
2 2
1 3

n 0
n-1 1
n-2 2
'''


'''
def f(x):
    x==0:
        return
    print(a)
    f(x-1)
    print(b)
'''