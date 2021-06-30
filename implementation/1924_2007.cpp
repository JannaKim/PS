#include <stdio.h>

using namespace std;

int main(){
    int m, d;
    scanf("%d %d", &m, &d);
    int date[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int tmp = 0;
    int day = 0;
    while(tmp + 1 != m){
        day += date[tmp];
        tmp = (tmp + 1) % 12;
    }
    day += d;
    //printf("%d", day);
    day %= 7;


    char *D[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    printf("%s", D[day ]);

}