#include <stdio.h>
using namespace std;
int main(){
    long long n;
    int l;
    scanf("%lld",&n);
    scanf("%d",&l);

    for(int i=l;i<=100;++i)
    {
        if(i%2==0)// if i even
        {
            double x= (double)n/i;
            long long y = (long long)x;
            if(x-y==0.5){// if n/i = x.5
                int cnt=i;
                long long len= y-(i/2-1);
                if(len<0){
                    printf("-1");
                    return 0;
                }
                while(cnt--){
                    printf("%lld ",len++);
                }
                return 0;
            }
        }
        else{// if odd
            long long y = (long long)n/i;
            if(n%i==0){//
                int cnt=i;
                long long len= y-i/2;
                if(len<0){
                    printf("-1");
                    return 0;
                }
                while(cnt--){
                    printf("%lld ",len++);
                }
                return 0;
            }
        }
    }
    printf("-1");

    
}


/*
4 3
-1

2 2
-1

5151 100
-1

30 6
-1

2 2
-1

14 2
2 3 4 5 

3 3
0 1 2

27 5
2 3 4 5 6 7 

36 8
1 2 3 4 5 6 7 8

147 4
22 23 24 25 26 27 

202 5
-1

1001 23
26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51

5050 99
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 


*/



/*

#include<iostream>
using namespace std;

int main() {
	int N, L; cin >> N >> L;
	
	for ( int k = L; k <= 100; k++ ) {
		for ( int u = max(0, N / k - k + 1); u <= N / k + 1; u++ ) {
			if ( ( ( u + k - 1 )*( u + k ) - u*( u - 1 ) ) / 2 == N ) {
				for ( int i = u; i < u + k; i++ ) {
					cout << i << " ";
				}
				return 0;	
			}
		}
	}
	cout << -1;
}

*/