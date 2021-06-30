#include <iostream>
#include <string>
#include <stdio.h>
#include <queue>
#include <vector>
using namespace std;

class Solution {
    private:
        pair<int, int> arr[26];
    public:
    vector<int> partitionLabels(string s) {
        struct compare{
            bool operator()(pair<int, int> a, pair<int, int> b){
                return a.first > b.first;
            }
        };
        for(int i = 0; i < 26; ++i){ //init
                arr[i].first = 1e9;
                arr[i].second = -1;
            }

            //for(auto it = s.begin(); it != s.end(); ++it){
            for(int i = 0; i < s.length(); ++i){    
                //printf("%d\n", s.at(i));
                if(i < arr[s.at(i) - 97].first) arr[s.at(i) - 97].first = i;
                if(i > arr[s.at(i) - 97].second) arr[s.at(i) - 97].second = i;
            }

            priority_queue <pair<int, int>, vector< pair<int, int> >, compare> pq;

            for(int i = 0; i < 26; ++i){    
                if(arr[i].first != 1e9){ // if exists
                    pq.push({arr[i].first, arr[i].second});
                }
            }

            vector<int> ans;

            

            pair <int, int> range = {1e9, 0};
            while(!pq.empty()){
                pair <int, int> tmp = pq.top();
                //cout << range.first <<' '<< range.second << '\n';
                pq.pop();
                if(boundaryout(range, tmp.first, tmp.second) == true){
                    if( range.first != 1e9 )
                        ans.push_back(range.second - range.first + 1);
                    range.first = tmp.first;
                    range.second = tmp.second;
                    continue;
                }
                if(range.second < tmp.second) range.second = tmp.second;
                if(tmp.first < range.first) range.first = tmp.first;

            }
        int sum_of_elems = 0;
        for (auto& n : ans)
            sum_of_elems += n;
        if(sum_of_elems != s.size())
            ans.push_back(range.second - range.first + 1);
        return ans;
    }
    
    bool boundaryout(pair <int, int> tmp, int lo, int hi){
            if(tmp.second < lo && tmp.second < hi) return true;
            if(hi < tmp.first && lo < tmp.first) return true;
            return false;
            }
};




