from operator import itemgetter
from sys import *; input = lambda: stdin.readline().rstrip()
word = []
for _ in range(int(input())):
    s = input()
    word.append((s, len(s)))
word=set(word)
word=list(word)
word.sort(key= itemgetter(1,0))

for a, b in word:
    print(a)

'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''