n= int(input())
given= input()
def test(picked, line):
    cnt=0
    start=0
    for el in line:
        if el!=picked:
            start=1
        if start and el==picked:
            cnt+=1
    return cnt


print(min(test('R', given), test('R', given[::-1]), test('B',given), test('B',given[::-1])))