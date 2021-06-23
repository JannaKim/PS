#include <stdio.h>
#include <stack>
#include <vector>
using namespace std;

vector <long long> ans;
long long ans2 = 1;
vector <long long> remain;
bool visited[21];
long long n;
/* 🐣🐥 */
long long fac(long long a){
    long long s = 1;
    for(long long i = 1; i < a + 1; ++i){
        s *= i;
    }
    return s;
}
void rec(long long nth, long long num){
    if(nth == 0){
        for(long long i = 0; i < remain.size(); ++i){
            ans.push_back(remain[i]);
        }
        return;
    }
    long long tmp = fac(num - 1);
    
    long long nxt = (nth) / tmp;
    //printf("%lld  ", nxt);
    ans.push_back(remain[nxt]);
    remain.erase(remain.begin() + nxt);
    rec(nth - (nxt)*tmp, num -1); 

}
void makeseq(){
    long long k;
    scanf("%lld", &k);
    ans.clear();
    remain.clear();
    for(long long i = 1; i < n + 1; ++i){
        remain.push_back(i);
    }
    rec(k - 1 , n); // 0 th ~ k - 1 th
    for(long long i = 0; i < ans.size();++i){
        printf("%lld ",ans[i]);
    }
    printf("\n");
}

void findseq(){
    long long ths;
    long long tmp = 0;
    //vector <long long> seq;
    //seq.push_back(0);
    for(long long i = 0; i < n; ++i){
        visited[i] = false;
        //scanf("%lld", &ths);
        //seq.push_back(ths);
    }
    
    for(long long i = 1; i < n + 1; ++i){
        scanf("%lld", &ths);
        for(long long j = 1; j < n + 1; ++j){
            if(ths == j){
                visited[ths] = true;
                break;
            }
            else if(visited[j] == false){
                ans2 += fac(n - i);
            }
            
        }
    }
    

    printf("%lld", ans2);
}
int main(){
    
    scanf("%lld\n", &n);

    long long a;
    scanf("%lld", &a);
    if(a == 1)
        makeseq();
    else
    {
        findseq();
    }
    

}