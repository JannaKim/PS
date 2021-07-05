#include <unordered_map>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    
    static bool comp(const pair<int, int> &a, const pair<int, int> &b){
        return (a.second > b.second);
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hm;
        int n = nums.size();
        for(int i = 0; i < n; ++i){
            if(hm.find(nums[i]) == hm.end())
                hm[nums[i]] = 0;
            hm[nums[i]] += 1;
        }
        
        vector< pair<int, int>> elems(hm.begin(), hm.end());
        sort(elems.begin(), elems.end(), comp);
        //vector< pair<int, int>> elems;
        //elems.assign(begin(hm), end(hm));
        //sort(begin(elems), end(elems), [&](auto l, auto r) {
        //    return l.second > r.second;
        //});
        
        vector <int> ans;
        ans.clear();
        for(int i = 0; i < k; ++i)
            ans.push_back(elems[i].first);
        return ans;
        
    }
    
};

/*
Runtime: 16 ms, faster than 68.60% of C++ online submissions for Top K Frequent Elements.
Memory Usage: 13.7 MB, less than 70.11% of C++ online submissions for Top K Frequent Elements.
Next challenges:

*/