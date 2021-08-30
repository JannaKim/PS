#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n, m;
vector < vector <char> >  board;

vector < vector <char> > input(){
    cin >> n; cin >> m;
    vector < vector <char> > board(n,vector <char>(m,0));
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            char piece;
            cin >> piece;
            char bit = (piece == 'W') ? 0b1 : 0b0;
            board[i][j] = bit;
        }
    }
    return board;
}

int test(int i, int j){
    int case1 = 0;
    int case2 = 0;
    for(int k = 0; k < 8; ++k){
        for(int l = 0; l < 8; ++l){
            char bit = board[i + k][j + l];
            if( k % 2 ){
                case1 += ((l%2) ^ bit) ? 1 : 0; //한 개의 피연산자만 1인 경우에만 1
                case2 += ((l%2) ^ bit) ? 0 : 1; 
            }
            else{
                case2 += ((l%2) ^ bit) ? 1 : 0;
                case1 += ((l%2) ^ bit) ? 0 : 1;        
            }
        }
    }
    
    return min(case1, case2);
}

int main(){
    board = input();
    int ans = 1e9;

    for(int i = 0; i <= n - 8; ++i){
        for(int j = 0; j <= m - 8; ++j){
            int tmp = test(i, j);
            ans = min(ans, tmp);
        }
    }
    cout << ans;
}