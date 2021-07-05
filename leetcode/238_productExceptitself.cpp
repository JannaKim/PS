#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int uniquezero = 0;
        int uniqueloc = -1;
        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] == 0){
                uniquezero++;
                uniqueloc = i;
                continue;
            }
            
            product *= nums[i];
        }

        vector<int> ans;
        ans.clear();
        if(uniquezero > 0){
        if(uniquezero == 1){
            
            for(int i = 0; i < nums.size(); ++i){
                if(i == uniqueloc) ans.push_back(product);
                else ans.push_back(0);
            }
            return ans;
            
        }
            else{
                for(int i = 0; i < nums.size(); ++i)
                    ans.push_back(0);
            
                return ans;
                
            }
        }
        for(int i = 0; i < nums.size(); ++i)
            ans.push_back(product/nums[i]);
        
        return ans;
        
    }
    
};


/*
Runtime: 28 ms, faster than 33.62% of C++ online submissions for Product of Array Except Self.
Memory Usage: 24.9 MB, less than 40.79% of C++ online submissions for Product of Array Except Self.
*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int left = 1;
        int right = 1;
        vector<int> ans;
        ans.clear();
        int n = nums.size();
        for(int i = 0; i < n; ++i){
            ans.push_back(1);
        }
        for(int i = 0; i < n; ++i){
            ans[i]*=left;
            left*=nums[i];
            ans[n - 1 - i]*=right;
            right*=nums[n - 1 - i];
        }
        return ans;
    }
    
};

/*
Runtime: 24 ms, faster than 60.59% of C++ online submissions for Product of Array Except Self.
Memory Usage: 25 MB, less than 34.00% of C++ online submissions for Product of Array Except Self.
*/