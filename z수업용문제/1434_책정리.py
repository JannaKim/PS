n, m = map(int, input().split())
stock=[int(i) for i in input().split()]
shelf=[int(i) for i in input().split()]

wasted=0
box=0
book=shelf.pop(0)
while True:
    if not box:
        box=stock.pop(0)
    if box>=book:
        box-=book
        if shelf:
            book=shelf.pop(0)
        else: 
            wasted+=box
            break

    if box<book:
        wasted+=box
        box=0
if stock:
    wasted+=sum(stock)
print(wasted)