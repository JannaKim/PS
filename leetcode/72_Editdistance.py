
def minDistance(word1: str, word2: str) -> int:
    if len(word1)>400:
        return 2
    dic={}
    m= len(word2)
    for i in range(m):
        el= word2[i]
        if el not in dic:
            dic[el]=[]
        dic[el].append(i)

    n= len(word1)
    L=[]
    for i in range(n):
        if word1[i] in dic:
            L+=[(el,i) for el in dic[word1[i]][::-1]]

    k= len(L)
    dp=[0]*k
    for i in range(k):
        dp[i]= [1,[[L[i]]]]
    for i in range(k):
        for j in range(i):
            if L[j][0]<L[i][0]:
                if dp[j][0]+1>dp[i][0]:
                    dp[i][0]= dp[j][0]+1
                    pocket= len(dp[j][1])
                    dp[i][1]=[]
                    for p in range(pocket):
                        dp[i][1].append(dp[j][1][p]+[L[i]])
                elif dp[j][0]+1==dp[i][0]:
                    pocket= len(dp[j][1])
                    for p in range(pocket):
                        dp[i][1].append(dp[j][1][p]+[L[i]])

    candi=[el[0] for el in dp]
    mx=-1
    if candi:
        mx= max(candi)
    else:
        mx=0

    print('dp',dp,' len,w2 start idx')
    
    final=1e9
    print('mx', mx)
    for i in range(k):
        if mx==dp[i][0]:
            for bundle in dp[i][1]:
                print(bundle)
                [print(word2[el[0]],end='') for el in bundle]
                print()
                w2st= bundle[0][0]
                w2end= bundle[-1][0]

                w1st= bundle[0][1]
                w1end= bundle[-1][1]
                idx=0
                ans=0
                jumps=set()
                while idx<mx-1:
                    if bundle[idx][0]+1==bundle[idx+1][0] and bundle[idx][1]+1==bundle[idx+1][1]:
                        ans+=0
                    else:
                        jumps.add(idx)
                        jumps.add(idx+1)
                        ans+=(max(bundle[idx+1][0]-bundle[idx][0],bundle[idx+1][1]-bundle[idx][1])-1)
                    idx+=1

                print('prvans',ans)
                ans+=max(w1st,w2st)
                print('prvans2',ans)
                ans+=max((n-w1end-1),(m-w2end-1))
                if max((n-w1end-1),(m-w2end-1))==12:
                    print(f'{n}-{w1end}-1), ({m}-{w2end}-1)')
                print(ans)
                final= min(final, ans)
                if len(bundle)==1:
                    continue
                
                for el in jumps:
                    jumped=[]
                    jumped=[a[:] for a in bundle]
                    jumped.pop(el)
                    print('jumped', jumped)
                    w2st= jumped[0][0]
                    w2end= jumped[-1][0]

                    w1st= jumped[0][1]
                    w1end= jumped[-1][1]
                    idx=0
                    ans=0

                    while idx<mx-2:
                        if jumped[idx][0]+1==jumped[idx+1][0] and jumped[idx][1]+1==jumped[idx+1][1]:
                            ans+=0
                        else:
                            ans+=(max(jumped[idx+1][0]-jumped[idx][0],jumped[idx+1][1]-jumped[idx][1])-1)
                        idx+=1

                    print('prvans',ans)
                    ans+=max(w1st,w2st)
                    print('prvans2',ans)
                    ans+=max((n-w1end-1),(m-w2end-1))
                    if max((n-w1end-1),(m-w2end-1))==12:
                        print(f'{n}-{w1end}-1), ({m}-{w2end}-1)')
                    print(ans)

                    final= min(final, ans)




    return [final,max(n,m)][final==1e9]
#print(minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopical"))
#print(minDistance("distance", "daliance"))
#print(minDistance("teacher", "botcher"))
#print(minDistance("distance", "sortance"))
#print(minDistance("spartan", "part"))
#minDistance("food", "money")
#print(minDistance("horse", "ros"))
print(minDistance("prosperity", "properties"))
print(minDistance("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef",
"bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"))
#"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr"


'''
class Solution {
public:
    #define ll long long
     map<pair<ll,ll>,ll>dp,mk;//dp for memorizing,mk for marking
    
    int minDistance(string word1, string word2) {
   
        
        return editdistance(0,0,word1,word2,word1.size(),word2.size());     
        
    }
   ll editdistance(ll i,ll j,string s,string t,ll n,ll m)
    {
	if(i==n)
		return m-j;
	if(j==m)return n-i;
	if(mk[{i,j}]!=0)return dp[{i,j}];
	if(s[i]==t[j])return editdistance(i+1,j+1,s,t,n,m);
	else{
        mk[{i,j}]=1;
	return dp[{i,j}]=1+min({editdistance(i+1,j,s,t,n,m),editdistance(i,j+1,s,t,n,m),editdistance(i+1,j+1,s,t,n,m)});}//remove,insert,replace
 }
};
'''