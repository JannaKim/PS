#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;
int N;
int half;
vector<int> ans;

void backtrack(int mask, int n, int cnt)
{
    
    if(cnt+N-n+1<half || n>N+1) return;
    if(cnt<half){
        backtrack( (mask<<1 | 1), n+1, cnt+1);
        backtrack( (mask<<1 | 0), n+1, cnt);
    }
    else ans.push_back(mask<<(N-(n-1)));
}


int main()
{
    scanf("%d\n",&N);
    half= N>>1;
    int mp[20+1][20+1]= {0, };

    int x;
    for(int i=1;i<N+1;i++)
        for(int j=1;j<N+1;j++)
        {
            scanf("%d",&x);
            if(i<j)
                mp[i][j]+=x;
            else
                mp[j][i]+=x;
        }

    backtrack(0, 1, 0);

    int mn=100*20+1;
    for(int occ:ans){
        int START=0;
        int LINK=0;
        for(int i=1;i<N;i++)
            for(int j=i+1;j<=N;j++)
            {
                int curI= 1<<(i-1);
                int curJ= 1<<(j-1);
                if( (occ& curI)&& (occ& curJ)) START+=mp[i][j];
                else if( ( (occ|curI) !=occ ) && ((occ|curJ) !=occ) ) LINK+=mp[i][j];
            }
        mn = min(mn,abs(START-LINK));
    }
    printf("%d",mn);

}

/*
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
*/


/*

#include<stdio.h>
#include<stdlib.h>

int table[22][22];
int r[22];
int c[22];
int min_num = 0x7fffffff;
int teams[22];
int n;
void dfs(int idx,int cnt,int total){
    if(cnt==n/2){
        if(min_num>abs(total)){
            min_num = abs(total);
        }
        return;
    }
    if(idx == n)return;
    dfs(idx+1, cnt+1,total -r[idx] - c[idx]);
    dfs(idx+1,cnt,total);
        
    
}
int main(){
    int tot=0;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            scanf("%d",&table[i][j]);
            tot+=table[i][j];
            c[i]+=table[i][j];
            r[j]+=table[i][j];
        }
    }
    dfs(1,1,tot-r[0]-c[0]);
    printf("%d",min_num);
    return 0;
}

*/