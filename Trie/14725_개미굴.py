import sys; input= lambda: sys.stdin.readline().rstrip()


class Trie():
    def __init__(self):
        self.nest={}
    
    def travel(self, L,pos,le):
        if pos==le:
            return
        if L[pos] not in self.nest:
            self.nest[L[pos]]=Trie()
        self.nest[L[pos]].travel(L, pos+1, le)

    def draw(self,story):
        for road in sorted(self.nest.keys()):
            print('-'*(story*2)+road)
            self.nest[road].draw(story+1)

n= int(input())

Antnest=Trie()
for _ in range(n):
    L=input().split()
    Antnest.travel(L[1:],0, int(L[0]))
Antnest.draw(0)