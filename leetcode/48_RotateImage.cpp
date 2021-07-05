#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    void swap(vector<vector<int>>& matrix, int y, int x, int ny, int nx){
        int tmp = matrix[y][x];
        matrix[y][x] = matrix[ny][nx];
        matrix[ny][nx] = tmp;
        return;
    }
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix[0].size();
        map<pair<int, int>, int> info;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                info.insert({ {i, j}, matrix[i][j] });
            }
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                cout << info.at({i, j}) <<" ";
            }
            cout<<"\n";
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                bool done = false;
                for(int a = 0; a < n; ++a){
                    for(int b = 0; b < n; ++b){
                        if(matrix[a][b] == info.at({i, j})){ //찾은 게 바꾸려는 좌표보다 왼쪽, 같다면 아래.
                            if(b > n -1 -i) continue;
                            if(b == n -1 -i && a < j) continue;
                            swap(matrix, a, b, j, n - 1 - i);
                            done = true;
                            break;
                        }
                    }
                    if(done == true) break;
                }
                if(done == false) return;
                
            }
        }
        //return matrix;
        
        
    }
};

/*
Runtime: 16 ms, faster than 61.10% of C++ online submissions for Rotate Image.
Memory Usage: 7.5 MB, less than 29.02% of C++ online submissions for Rotate Image.
*/