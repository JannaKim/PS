import sys; sys.setrecursionlimit(25000)
class Trie:
    def __init__(self):
        self.child={}
        self.cnt=0

    def insert(self, idx, w,ln):
        self.cnt+=1
        if idx==ln:
            return
        if idx==-1:
            if ln not in self.child:
                self.child[ln]=Trie()
            self.child[ln].insert(idx+1,w,ln)
        else:
            if w[idx] not in self.child:
                self.child[w[idx]]=Trie()
            self.child[w[idx]].insert(idx+1,w,ln)

    def find(self, idx, w,ln):
        if idx==-1:
            if ln in self.child:
                return self.child[ln].find(idx+1,w,ln)
            else:
                return 0
        else:
            if w[idx]=='?':
                return self.cnt
            else:
                if w[idx] not in self.child:
                    return 0
                else:
                    return self.child[w[idx]].find(idx+1,w,ln)



def solution(words, queries):
    answer = []
    FTree=Trie()
    BTree=Trie()

    for word in words:
        ln=len(word)
        FTree.insert(-1,word,ln)
        BTree.insert(-1,word[::-1], ln)

    for query in queries:
        if query[-1]=='?':
            answer.append(FTree.find(-1,query,len(query)))
        else:
            answer.append(BTree.find(-1,query[::-1],len(query)))

        
    
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao",'s1','s2','ab'],["fro??", "????o", "fr???", "fro???", "pro?",'??']))