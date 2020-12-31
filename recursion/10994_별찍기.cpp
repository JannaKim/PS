#include <stdio.h>
#include <string>
using namespace std;

int n;
int widesestSide;
void draw(int remain, int form);

int Tseq(int num){
    return 1+4*(num-1);
}

void wrap(int shell, int form)
{
    int side= Tseq(shell);
    int remain = (widesestSide-side)>>1;
    draw(remain, form);
    if(shell==1) return;
    if(form) wrap(shell-1, form^1); //XOR: 두 비트 다를 때 1
    else wrap(shell,form^1);
    draw(remain, form);

}

void draw(int remain, int form)
{
    if(form==0)
    {   
        
        for(int i=1; i<=widesestSide;++i)
        {
            if((i<=remain||i>=widesestSide-remain) && (i%2==0)) printf(" ");
            else printf("*");
        }
        printf("\n");
    }
    else{

        for(int i=1; i<=widesestSide;++i)
        {
            if((i<=remain+1||i>=widesestSide-remain-1) && (i%2)) printf("*");
            else printf(" ");
        }
        printf("\n");
    }
}

int main()
{
    scanf("%d",&n);
    widesestSide= Tseq(n);
    wrap(n,0);
    
}




/*
#include <iostream>
char starArr[400][400];
void star(int x, int y, int n) {
	if (n == 1) {
		starArr[x][y] = '*';
		return;
	}
	for (int i = 0; i < 4 * n - 3; ++i) {
		starArr[x][y + i] = '*'; //지붕
		starArr[x + 4 * n - 4][y + i] = '*'; //우벽
		starArr[x + i][y + 4 * n - 4] = '*'; //바닥
		starArr[x + i][y] = '*'; //좌벽
	}
	star(x + 2, y + 2, n - 1);
}
int main() {
	int n;
	std::cin >> n;
	for (int i = 0; i < 4 * n - 3; ++i) {
		for (int j = 0; j < 4 * n - 3; ++j) {
			starArr[i][j] = ' ';
		}
	}
	star(0, 0, n);
	for (int i = 0; i < 4 * n - 3; ++i) {
		std::cout << starArr[i] << "\n";
	}
}
*/