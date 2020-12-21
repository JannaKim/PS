package programmers;
import java.util.*;
public class DollPush {
    
}

//import java.util.Arrays; 
//import java.util.Collections; 
//import java.util.List;






class Solution {
    public int solution(int[][] board, int[] moves) {
        int n = board[0].length();
        List<Integer> list = Arrays.asList(board);
        Collections.reverse(list);
        reversed_board = list.toArray(new Integer[list.size()]);
        
        int[][] newboard= new int[n][];

        for(int i=0;i<n+1;i++) //배열안에 큐 넣기
            newboard[i]= new LinkedList<>();
        

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
                if(reversed_board[i][j]!=0) newboard[i+1].add(reversed_board[i][j]);
        }
        
        for(int i=0;i<n;i++){
            for(int j=0; j<reversed_board[i].size();j++){
                System.out.println(reversed_board[i][j]);
            }
        }
        
        
        
        int answer = 0;
        return answer;
    }
}
/*
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
    for(auto it: moves){
        if(newboard[it].empty())
            continue;
        auto doll = newboard[it].back();
        newboard[it].pop_back();
        if(!bucket.empty() && bucket.back() == doll){
            answer+=2;
            bucket.pop_back();
        }
        else
            bucket.push_back(doll);
    }
    return answer;
}
*/
//[1,5,3,5,1,2,1,4]
