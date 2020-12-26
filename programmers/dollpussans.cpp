#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int n = board.size();
    
    vector<vector<int> > newboard;
    
    for(int i=0;i<n+1;i++)
        newboard.push_back({});
    
    reverse(board.begin(), board.end());
    
    for(auto it: board){
        for(int i=0;i<n;i++)
            if(it[i]!=0) newboard[i+1].push_back(it[i]);
    }
    
    vector<int> bucket;
    //bucket.push_back(-1);
    for(auto it: moves){
        //printf("%d, ",it);
        //for(auto b: bucket) printf("%d ",b);
        //printf("\n");
        if(newboard[it].empty())
            continue;
        auto doll = newboard[it].back();
        newboard[it].pop_back();
        if(!bucket.empty() && bucket.back() == doll){
            //printf("%d %d\n",bucket.back(),doll);
            answer+=2;
            bucket.pop_back();
        }
        else
            bucket.push_back(doll);
    }
    return answer;
}

//[1,5,3,5,1,2,1,4]