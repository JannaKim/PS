import sys;
sys.setrecursionlimit(200000)

class Trie:
    def __init__(self) :
        self.count = 0
        self.child = {} 
    def insert(self, s, pos) :
        self.count = self.count + 1
        if pos == len(s) :
            return
        if s[pos] not in self.child:
            self.child[s[pos]]= Trie()
        self.child[s[pos]].insert(s,pos+1)

    def find(self, s, pos) :
        if self.count ==1:
            return pos
        elif pos==len(s):
            return pos
        else:
            return self.child[s[pos]].find(s,pos+1)


def solution(words):
    ans=0
    Hello= Trie()
    for word in words:
        Hello.insert(word, 0)

    for word in words:
        ans+=Hello.find(word,0)
    return ans

    

print(solution(["word","war","warrior","world"]	))