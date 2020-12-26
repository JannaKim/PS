#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int n= board.size();
    
    vector<vector<int>> newboard;
    for(int i=0; i<n;i++)
    {
        newboard.push_back()
    }

    for(auto it: reverse(board)){
        for(int i=0;i<n;i++){
            if(it[i]!=0) newboard[i].push_back(it[i]);
        }
    }

    
    int doll=0;
    for(int i=0;i<moves.size();i++){
        int address= moves[i]-1;
            if(newboard[address]
            newboard[address].front_pop?()
            doll=board[-board[0][address]][address];
            if(basket.back()==doll) basket.pop_back();
            else basket.push_back(doll);
            board[0][address]-=1; 
        }
        else if(board[0][address]>0){
            if(board[0][address]==-2) continue;
            doll=board[0][address];
            if(basket.back()==doll) basket.pop_back();
            else basket.push_back(doll);
            board[0][address]= -1; 
        }
        else {
            int floor =0;
            while(board[floor][address]==0)++floor;
            if(floor==n) continue;
            doll=board[floor][address];
            if(basket.back()==doll) basket.pop_back();
            else basket.push_back(doll);
            board[0][address]= -floor-1; 
        }
    answer= basket.size()-1;
    }
    return answer;
}