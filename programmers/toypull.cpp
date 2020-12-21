#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> basket;
    basket.push_back(-2);
    
    vector<int> temp;
    for(int i=0;i<board[0].size();i++)
        temp.push_back(0);
    board.push_back(temp);
    int doll=0;
    for(int i=0;i<moves.size();i++){
        int address= moves[i]-1;
        if(board[0][address]<0){
            if(board[-board[0][address]][address]==-2) continue;
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
            while(floor==0)++floor;
            if(board[floor][address]==-2) continue;
            doll=board[floor][address];
            if(basket.back()==doll) basket.pop_back();
            else basket.push_back(doll);
            board[0][address]= -floor-1; 
        }
    answer= basket.size()-1;
    }
    return answer;
}