#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

/*
 46. Permutations
 Given an array nums of distinct integers, return all the possible permutations. 
 You can return the answer in any order.
 
 1 <= nums.length <= 6
 -10 <= nums[i] <= 10
 All the integers of nums are unique.
  
 */
void print(vector<int> v){

    for(auto el: v)
        printf(" %d,",el);
    printf("\n");

}

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
       // swap으로 모든 permutation을 만들 수 있음.
       // 특정 자리에 특정 값이 고정된 경우 나머지들로 만든 permute의 합.
       vector<vector<int>> answer;
       permuteHelper(nums, answer, nums.size());

       return answer;


    }
    void permuteHelper(vector<int> nums, vector<vector<int>>& answer, int length ){
        print(nums);
        // if length == 1, nothing to swap
        if (length == 1){
            answer.push_back(nums);
            return;
        }

        for(int i = 0; i < length; i++){
            // fix the last elt
            permuteHelper(nums, answer, length-1);
            swap(nums[i], nums[length-1]);
            // if (length %2 == 1){
            //     swap(nums[0], nums[length-1]);
            //     if (i >= 1) break;
            // }
            // else {
            //     swap(nums[i], nums[length-1]);
            // }

        }


    }
};



void print(vector<vector<int>> &v){
    printf("[\n");
    for(int i=0; i<v.size()-1; i++){
        printf("\t");
        print(v[i]);
 
    }
    printf("\t");
    print(v[v.size()-1]);
    printf("]\n\n");
        
    
}
int main(){

    Solution sol;
    vector<int> nums{1,2,3};
    vector<vector<int>> v = sol.permute(nums);
    print(v);
    nums = {0,1};
    //v = sol.permute(nums);
    //print(v);
    nums = {1};
    //v = sol.permute(nums);
    //print(v);
}


/*

Runtime: 4 ms, faster than 75.01% of C++ online submissions for Permutations.
Memory Usage: 7.9 MB, less than 46.74% of C++ online submissions for Permutations.
*/
