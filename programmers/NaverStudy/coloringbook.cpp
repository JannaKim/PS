#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;
static int dy[4]= {0,0,1,-1};
static int dx[4]= {1,-1,0,0};
void dfs(int y, int x, int el);
int M;
int N;
int chk[100+1][100+1];
vector<vector<int>> picture;


// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    M=m;
    N=n;
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    //int chk[m][n]= {0,}; //bool? ?

    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            if(chk[i][j]==0 && picture[i][j]>0){
                chk[i][j]=1;
                number_of_area++;
                dfs(i,j, picture[i][j]);
                int tmp=0;
                for (int a=0;a<m;++a)
                    for(int b=0;b<n;++b)
                        if((chk[a][b]==1) && (picture[i][j]>0))
                        {   
                            picture[i][j]=0;
                            tmp++;
                        }
                max_size_of_one_area= max(max_size_of_one_area, tmp);
            }
        }
    }

    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

void dfs(int y, int x, int el){
    for(int i=0;i<4;++i)
    {
        int ny= y+dy[i];
        int nx= x+dx[i];
        if(ny<0||ny>=M||nx<0||nx>=N) continue;
        if((picture[ny][nx]==el)&&(chk[ny][nx]==0)){
            chk[ny][nx]=1;
            dfs(ny,nx,el);
        }
    }


}

int main(){
    /*
    vector<vector<int>> vect; 
    vect.push_back(10); 
    vect.push_back(20); 
   
    func(vect); 
    cout<<solution(6,4,[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]);
    */
}