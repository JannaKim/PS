#include <stdio.h>
char find(int a, int b, int c, int d){
    int sum = a + b + c + d;
    switch(sum){
        case 0:
            return 'D';
        case 1:
            return 'C';
        case 2:
            return 'B';
        case 3:
            return 'A';
        case 4:
            return 'E';
    }
}
int main(){
    for(int i = 0; i < 3; ++i){
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        printf("%c\n", find(a, b, c, d));
    }
}