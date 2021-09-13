
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
#define ll long long int

vector <ll> basket;
ll factorial[21] = {0};

void fac(){
    ll res = 1;
    factorial[0] = 1;
    for(ll i = 1; i <= 20; ++i){
        res *= i;
        factorial[i] = res;
    }
}

void print(vector <ll> v){
    for(auto it : v) cout << it << " ";
    cout << "\n";
}

void set(ll k, vector<ll> &ans){
    ans.push_back(basket[k - 1]);
    basket.erase(basket.begin() + k - 1);
}

vector <ll> kth(ll n, ll k){
    vector <ll> ans;
    for(ll i = n - 1; i >= 1; --i){
        ll permu = factorial[i]; 
        ll j;
        for(j = 1; j <= i; j++){
            if(permu >= k) break; // number of permu in my(k) back. 
            k -= permu ; // k should always be k>=1
        }
        set(j, ans);
    }
    ans.push_back(basket[0]);
    return ans;
}


ll measure(vector<ll> seq, ll n){
    ll res = 0;
    for(ll i = 0; i < n; ++i){
        ll cnt = 0;
        for(ll j = i + 1; j < n; ++j){
            if(seq[i] > seq[j]) ++cnt;
        }
        res += cnt * factorial[n - 1 - i];
    }
    ++res;
    return res;
}
int main(){
    ll n, q;
    cin >> n >> q;
    for(ll i = 1; i <= n; ++i){
        basket.push_back(i);
    }

    fac();

    
    if(q == 1) {
        ll k;
        cin >> k;
        vector <ll> ans;
        ans = kth(n, k);
        print(ans);
    }
    else{
        vector<ll> seq(n, 0);
        for(ll i = 0; i < n; ++i) cin >> seq[i];
        ll ans = measure(seq, n);
        cout << ans;
    }
}