#include <iostream>
#include <map>
#include <vector>
using namespace std;
const int MAX = 40000;
typedef long long ll;

int n;
map<int, int> groups;
vector<int> primes;
bool vis[MAX];

void search(int x);

int main(){
    for(int i = 2; i < MAX; ++i){ // find all primes using net 
        if(vis[i]) continue;
        primes.push_back(i);
        for(int j = 2 * i; j < MAX; j += i)
            vis[j] = true;
    }

    while(1){
        cin >> n;
        if(n == 0) break;
        groups.clear();
        search(n);
        ll ans = 1LL;
        for(auto it : groups){ // all m, n s that are in φ(mn) = φ(m)φ(n) are measured before.
            int p = it.first;
            int k = it.second;
            // use φ(p^k) = p^(k-1) x (p-1). simply multiply them.
            --k;
            while(k--) ans*=p; // p^(k-1)
            ans *= (p - 1); // (p-1)
        }
        cout << ans << '\n';
    }

}


void search(int x){
    if(x == 1) return;
    for(auto num : primes){
        if(x % num == 0){ // found : 2 or 5 in φ(20) = φ(2^2 * 5)
            ++groups[num];
            search(x / num); // 10 is also divisible with 2, so two 2 could be found.
            return; // only once. 20 / 2 handles second 2
        }
    }
    if(x != 1) ++groups[x]; // if x == 20 and prime = 7, is should also be grouped.
}


