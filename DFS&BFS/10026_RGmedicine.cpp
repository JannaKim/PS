#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)
#define FORR(i,n) for(int i=1;i<=n;++i)
void fill(int i,int j,int color);
vector<vector<int>> grid;
vector<int>line;
int isntRGM[5];
int isRGM;
int main()
{
    int n;
    scanf("%d\n",&n);
    FOR(i,n+2) line.push_back(-1);
    grid.push_back(line);
    
    FOR(i,n){
        line.clear();
        line.push_back(-1);
        string s;
        getline(cin,s,'\n');
        FOR(j,n){
            if(s[j]=='R') line.push_back(1);
            else if(s[j]=='G') line.push_back(2);
            else line.push_back(3);
        }
        line.push_back(-1);
        grid.push_back(line);
    }
    line.clear();
    FOR(i,n+2) line.push_back(-1);
    grid.push_back(line);

    FORR(i,n) FORR(j,n) if(grid[i][j]>=1){
        isntRGM[grid[i][j]]+=1;
        fill(i,j,grid[i][j]);
    }
  
    FORR(i,n) FORR(j,n) if(grid[i][j]==0){
        isRGM+=1;
        fill(i,j,grid[i][j]);
    }
    printf("%d %d",isntRGM[1]+isntRGM[2]+isntRGM[3],isRGM+ isntRGM[3]);
    
}
int d[][2] = {0,1, 1,0, 0,-1, -1,0};
void fill(int i,int j,int color){
    if((0<color)&&(color<3)) grid[i][j]=0; //0: color for RGM
    else grid[i][j]=-1; //1) B->-1 , 2) RG->-1
    FOR(k,4)
        if(grid[i+d[k][0]][j+d[k][1]]==color)
            fill(i+d[k][0],j+d[k][1],color);  
}


/*
#include <iostream>
using namespace std;
int n, ans, v[105][105];
char a[105][105];

void f(int p, int q, char c) {
	if(v[p][q] || a[p][q]!=c) return;
	v[p][q] = 1;
	f(p+1, q, c);
	f(p-1, q, c);
	f(p, q+1, c);
	f(p, q-1, c);
}

int main() {
	int i, j;
	cin>>n;
	for(i=1; i<=n; i++) cin>>a[i]+1;
	for(i=1; i<=n; i++) for(j=1; j<=n; j++) if(!v[i][j]) {
		ans++;
		f(i, j, a[i][j]);
	}
	cout<<ans<<' ';
	for(i=1; i<=n; i++) for(j=1; j<=n; j++) {
		v[i][j] = 0;
		if(a[i][j]=='G') a[i][j] = 'R';
	}
	ans = 0;
	for(i=1; i<=n; i++) for(j=1; j<=n; j++) if(!v[i][j]) {
		ans++;
		f(i, j, a[i][j]);
	}
	cout<<ans;
	return 0;
}
*/