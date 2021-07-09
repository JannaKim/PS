#include <iostream>
#include <stdio.h>
#include <vector>
#include <sstream>
using namespace std;

vector<string> split(string str, char delimiter);
int main(){
    string ths;
    cin >> ths;
    vector<string> ans;
    ans = split(ths, ' ');
    for(int i = 0; i < ans.size(); ++i){
        cout <<ans[i]<<' ';
    }

}


vector<string> split(string input, char delimiter){
    vector<string> answer;
    stringstream ss(input);
    string tmp;
    while(getline(ss, tmp, delimiter)){
        string rv;
        cout<<tmp<<' ';
        for(int i = tmp.size() - 1; i >=0; --i){
            rv += tmp.substr(i, 1);
        }
        answer.push_back(rv);
    }
    return answer;
}