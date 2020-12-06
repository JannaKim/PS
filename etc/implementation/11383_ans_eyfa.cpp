#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int main() {
	int n, m;
	scanf("%d %d",&n,&m);
	char s1[10][11], s2[10][21];
	for(int i=0;i<n;i++)
    {
		scanf("%s",s1[i]);
        cout<<s1[i];
    }
	for(int i=0;i<n;i++)
		scanf("%s",s2[i]);
	for(int i=0;i<n;i++) {
		for(int j=0;j<m;j++) {
			if(s1[i][j]!=s2[i][j*2] || s1[i][j]!=s2[i][j*2+1]) {
				puts("Not Eyfa"); return 0;
			}
		}
	}
	puts("Eyfa");
}
