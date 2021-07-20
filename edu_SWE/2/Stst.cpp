#include <stdio.h>
#include <iostream>
using namespace std;
#define MAX_N 10
#define MAX_M 5
#define swap(type, y, x) do{type t = *y; *y = *x; *x = t;}while(0)
struct Result {
	int y, x;
};
int n = 10;
int m = 5;
int map[MAX_N][MAX_N] = 
{
    {0,0,0,0,0,0,0,0,0,0},
    {1,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {1,1,0,0,0,0,0,0,0,0},
    {0,1,0,1,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {1,1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1,1}
};


void init(int N, int M, int Map[MAX_N][MAX_N])
{
    n = N;
    m = M;
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j)
            map[i][j] = Map[i][j];
    }

}

void print(int(* stars)[MAX_M]){
    cout<<"\n";
    for(int i = 0 ; i < m; ++i){
        for(int j = 0; j < m; ++j){
            cout<<stars[i][j]<<" ";
        }
        cout<<"\n";
    }
}
int bound(int y, int x){
    if (y < n && x < n) return 1;
    return 0;
}
int match(int r, int c, int(* stars)[MAX_M]){
    cout<<"match"<<r<<" "<<c<<'\n';
    int i, j, si, sj;
    for(i = r, si = 0; i < r + m; ++i, ++si){
        for(j = c, sj = 0; j < c + m; ++j, ++sj){
            if(!bound(i, j)){ cout<<r<<" "<<c<<"bound \n";return 0;}
            if(stars[si][sj] && !map[i][j]){ cout<<i<<" "<<j<<" o x \n";return 0;}
            if(!stars[si][sj] && map[i][j]){ cout<<i<<" "<<j<<" x o \n";return 0;}

            // if(!bound(i, j)){ return 0;}
            // if(stars[i][j] && !map[i][j]){return 0;}
            // if(!stars[i][j] && map[i][j]){ return 0;}
        }
    }
    return 1;
}

void findMainStar(int c, int r, int(* stars)[MAX_M],struct Result *res){
    int i, j, si, sj;
        for(i = r, si = 0; i < r + m; ++i, ++si){
            for(j = c, sj = 0; j < c + m; ++j, ++sj){
                if(stars[si][sj] == 9){
                    cout<<i<<" "<<j<<"\n";
                    (*res).y = i;
                    (*res).x = j;
                    return;
                }
        }
    }

}

void rotate(int(* stars)[MAX_M]){
    for(int i = 0; i < m; ++i){
        for(int j = i + 1; j < m; ++j){
            swap(int, &stars[i][j], &stars[j][i]);
        }
    }

    for(int i = 0; i < m; ++i){
        for(int j = 0; j < m/2; ++j){
            swap(int, &stars[i][j], &stars[i][m - 1 - j]);
        }
    }
}

void traverse(int(* stars)[MAX_M], struct Result *res){
    for(int dir = 0; dir < 4; ++dir){
        print(stars);
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                if(match(i, j, stars)){
                    cout<<"match!!!!!!"<<i<<" "<<j<<'\n';
                    findMainStar(i, j, stars, res);
                    return;
                }
            }
        }
        rotate(stars);
    }
}
Result res;
Result findConstellation(int stars[MAX_M][MAX_M])
{
	
	res.y = res.x = 0;
    traverse(stars, &res);
    printf("%d %d", res.y, res.x);
	return res;
}

int main(){
    Result ans;
    int s[5][5] = {{0,0,1,0,1}, {0,1,1,0,0}, {0,0,0,0,0}, {0,9,0,0,0}, {0,0,0,0,0}};
    ans = findConstellation(s);
    
}


/*

0 0 1 0 1 
0 1 1 0 0 
0 0 0 0 0 
0 9 0 0 0 
0 0 0 0 0 

0 0 0 0 1 
0 0 0 9 0 
0 1 0 0 0 
0 1 0 0 0 
0 0 1 0 0 

*/