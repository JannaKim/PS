import sys; input= lambda: sys.stdin.readline().rstrip()

class Trie():
    def __init__(self):
        self.child={}
        self.last=False
    
    def insert(self, s, pos, le):
        if pos==le:
            self.last=True
            return True
        else:
            if self.last==True:
                return False
        if s[pos] not in self.child:
            self.child[s[pos]]=Trie()
        return self.child[s[pos]].insert(s, pos+1, le)



for _ in range(int(input())):
    n= int(input())
    New= Trie()
    L=[]
    for _ in range(n):
        L.append(input())
    L.sort()
    for num in L:
        flag=True
        if not New.insert(num, 0, len(num)):
            flag=False
            print('NO')
            break
    if flag:
        print('YES')

        