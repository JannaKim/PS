/*
malloc, calloc, free 연습
+ C 언어 메모리 구조
*/

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h> // 말록 라이브러리

#define swap(type, x, y) type t = x; x = y; y = t;
#define swap2(type, x, y) do{type t = x; x = y; y = t;}while(0)
using namespace std;

//define NULL ((void *)0) // stdio.h 에 있다.
int won[] = {1, 2, 5, 7}; // 크기 4로 자동 선언. 데이터 영역에 정적 배열 할당. 프로그램 시작 시 항당, 종료시 메모리에서 해제
//int dp[100000 + 10];

int main(){
    int a = 2;
    int b = 1;
    if(a < b){
        swap(int, a, b)
    }
    else
    {
        swap2(int, b, a);
    }
    
    cout << a <<' '<<b<<'\n';
    //fill(&dp[0], &dp[100000 + 10], (int)1e9);
    //dp[0] = 0;
    int n;
    scanf("%d", &n);
    // void *calloc(size_t nmemb, size_t size);
    int *dp = (int *)calloc(n + 1, sizeof(int)); // 0으로 초기화
    free(dp); // dp 포인터가 가리키는 메모리를 해제.
    dp = (int *)malloc((n + 10) * sizeof(int)); // 힙 영역

    *dp = 0;
    for(int i = 1; i <= n + 9; ++i){ // !! 무조건 쓰는거 다 초기화 해줘야함
        *(dp + i) = (int)1e9;
    }

    int nmOfwon = sizeof(won)/sizeof(won[0]); //배열 요소의 개수 구하기

    for(auto it: won){
        for(int i = 0; i <n + 1; ++i){
            if(!i) *(dp + it) = 1;
            else if(*(dp + i) != (int)1e9) dp[i + it] = min(dp[i + it], dp[i] + 1);
        }
    }
    cout << *(dp + n);

    return 0;
}