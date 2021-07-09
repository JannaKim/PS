#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

string s;
int main(){
    while(true){
        cin >> s;
        if(s == "*") break;
        vector<unordered_map<string, bool>> H;
        for(int i = 0; i < s.size(); ++i){
            unordered_map<string, bool> tmp;
            H.push_back(tmp);
        }
        bool flag = false;
        for(int i = 0; i < s.size(); ++i){
            for(int j = i + 1; j < s.size(); ++j){
                int space = j - i;
                auto it = H[space].find(s.substr(i, 1) + s.substr(j, 1)); // substr!
                if(it == H[space].end()){ // char + char 이라서 오류났을 듯
                    H[space].insert({s.substr(i, 1) + s.substr(j, 1), true});
                }
                else{
                    flag = true;
                    break;
                }

            }
            if(flag==true) break;

        }
        string ans = (flag == true) ? "is NOT surprising." : "is surprising.";
        cout<<s<<' '<<ans<<'\n';
        

    }

    //getline(cin, s);
    //s = "";
    //s += s[i];
    //(cin >> n).get(); // 개행문자 빼기 getline(cin, a);
    //word.substr(1); 1부터 쭉 
}