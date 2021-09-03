/*

#include <bits/stdc++.h>

int main() {
    using namespace std;
    ios::sync_with_stdio(0), cin.tie(0);

    string s, t; cin >> s >> t;

    function<bool(string)> chk;
    chk = [&](string x) -> bool {
        if (x == s) return 1;
        if (x.empty()) return 0;
        if (x.back() == 'A') {
            string tmp(x);
            tmp.pop_back();
            if (chk(tmp)) return 1;
        }
        if (x.front() == 'B') {
            string tmp(x);
            reverse(begin(tmp), end(tmp));
            tmp.pop_back();
            if (chk(tmp)) return 1;
        }
        return 0;
    };
    
    cout << chk(t);
}

*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    string s, t;
    cin >> s >> t;

    function<bool(string)> search;

    search = [&](string x) -> bool {
        if(x.size() == s.size()) return x == s;

        if(x.back() == 'A'){
            x.pop_back();
            if(search(x)) return true;
            x.push_back('A');
        }

        if(x.front() == 'B'){
            reverse(x.begin(), x.end());
            x.pop_back();
            if(search(x)) return true;
            x.push_back('B');
            reverse(x.begin(), x.end());
        }
        return false;
    };
    cout << search(t);
}