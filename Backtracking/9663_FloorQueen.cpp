#include <stdio.h>
bool isValid(int floor, int queen);
void backtracking(int floor);
void chessboard(int board);
int n;
int board[15];
int ans=0;

int main()
{
    scanf("%d",&n);
    backtracking(0);
    printf("%d",ans);
}

void backtracking(int floor)
{
    //if(n-floor+num<n) return;
    if(floor==n){ans+=1; return;}
    for(int i=0;i<n;++i)
    {
        if(isValid(floor,i)){
            //if(num==n){ans+=1; return;}
            board[floor]=i;
            backtracking(floor+1);
        }

    }
    //backtracking(floor+1,num); 한칸띄면 N 개의 queen 배치 불가능
}

bool isValid(int floor, int queen)
{
    for(int i=0;i<floor;++i)
    {
        if(board[i]==queen) return 0;
        if(floor-i==queen-board[i]) return 0;
        if(floor-i==board[i]-queen) return 0;
    }
    return 1;

}
/*
void chessboard(int board)
{
    for(int i=0; i<n*n; ++i)
    {
        int mask=1<<i;
        ((board&mask)?printf("1"):printf("0"));
        if((i%n)==n-1) printf("\n");
    }
    printf("\n");
}
*/


/*
#include<stdio.h>
bool a[15][15],v[15],h[15],u[30],d[30];
int N,R;
void f(int i){
	if(i==N)++R;
	for(int j=0;j<N;++j){
		if(v[j]||h[i]||u[i+j]||d[i-j+N])continue;
		v[j]=h[i]=u[i+j]=d[i-j+N]=1;
		f(i+1);
		v[j]=h[i]=u[i+j]=d[i-j+N]=0;
	}
}
int main(){
	scanf("%d",&N);
	f(0);
	printf("%d",R);
}
*/