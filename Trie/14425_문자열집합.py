import sys; input= lambda: sys.stdin.readline().rstrip()
class Trie:
    def __init__(self):
        self.child={}
        self.end=False

    def insert(self, s, pos, le):
        if pos==le:
            self.end=True
            return
        if s[pos] not in self.child:
            self.child[s[pos]]=Trie()

        self.child[s[pos]].insert(s,pos+1,le)

    def find(self, s, pos, le):
        if pos==le:
            return self.end
        else:
            if s[pos] in self.child:
                return self.child[s[pos]].find(s,pos+1,le)
            else:
                return False



n, m= map(int, input().split())
root= Trie()
for _ in range(n):
    inp=input()
    root.insert(inp, 0, len(inp))

ans=0
for _ in range(m):
    qu= input()
    if root.find(qu, 0, len(qu)):
        ans+=1
print(ans)


