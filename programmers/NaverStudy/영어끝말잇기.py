# 10 min
def solution(n, words):
    dic={}
    end=' '
    for i, w in enumerate(words):
        #print(end,w)
        if w not in dic and (end==' ' or w[0]==end):
            dic[w]=True
        else:
            return [i%n+1,i//n+1]
        end=w[-1]
    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))