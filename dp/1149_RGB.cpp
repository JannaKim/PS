#include <stdio.h>
#include <algorithm>
using namespace std;
int minCost[100000+1][3+1]={0,};
int main()
{
    int n;
    scanf("%d",&n);
    
    int r, g, b;
    scanf("%d %d %d",&r, &g, &b);
    minCost[0][0]= r;
    minCost[0][1]= g;
    minCost[0][2]= b;
    int i;
    for(i=1;i<n;++i)
    {
        int r, g, b;
        scanf("%d %d %d",&r, &g, &b);
        minCost[i][0]= min(minCost[i-1][1], minCost[i-1][2])+ r;
        minCost[i][1]= min(minCost[i-1][0], minCost[i-1][2])+ g;
        minCost[i][2]= min(minCost[i-1][0], minCost[i-1][1])+ b;
    }
    printf("%d",min({minCost[n-1][0], minCost[n-1][1],minCost[n-1][2]}));
}



/*
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int n, r, g, b, c[3] = { 0, }; scanf("%d", &n);
	while (n--) {
		scanf("%d %d %d", &r, &g, &b);
		r += min(c[1], c[2]);
		g += min(c[0], c[2]);
		b += min(c[0], c[1]);
		c[0] = r, c[1] = g, c[2] = b;
	}
	printf("%d", min(r, min(g, b)));
}

int main(){
    int n;
    scanf("%d",&n);
    int dp[100][2]={0,};
    dp[0][0]=1;
    dp[0][1]=1;
    for(int i=1;i<n;i++)
    {
        dp[i][0]=dp[i-1][1];
        dp[i][1]= dp[i-1][0]+dp[i-1][1];
    }
    printf("%d",dp[n-1][0]+dp[n-1][1]);
}

int main(){
    int n;
    scanf("%d",&n);
    int a=1, b=1;
    for(int i=1;i<n;i++)
    {
        int previous_a=a, previous_b=b;
        a = previous_b;
        b= previous_a+ previous_b;
    }
    printf("%d",a+b);
}

*/