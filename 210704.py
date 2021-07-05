#L = [i for i in range(1, int(1e15) + 1)]
#print(len(L))


L = (i for i in range(1, int(1e15) + 1))
'''
쓰레드 하나가 저걸 갖고 있는데
유저레벨 쓰레드인데
포문에서 한 값 요청 할 때마다 값을 뱉어줄 뿐
'''
#print(len(L))
#print(L)
#for el in L:
#    print(el)
print(range(2, 10))