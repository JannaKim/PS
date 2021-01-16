#include <algorithm>
#include <stdio.h>
#include <vector>
#define v vector
#define print printf
#define ts "%d",
#define pb push_back
#define FOR(i,n) for(int i=0;i<n;++i)
using namespace std;

int main()
{
    int n;
    scanf(ts &n);
    v <int> nums;
    FOR(i,n)
    {
        int x;
        scanf(ts &x);
        nums.pb(x);
    }
    sort(nums.begin(), nums.end());
    int m;
    scanf(ts &m);
    int a, b, mid, left, right;
    FOR(i,m)
    {
        int x;
        scanf(ts &x);
        a=0;
        b=n-1;
        left=-1;
        while(a<=b)
        {
            mid=(a+b)>>1;
            if(nums[mid]<x){
                left=mid;
                a=mid+1;
            }
            else b=mid-1;
        }
        a=0;
        b=n-1;
        right=-1;
        while(a<=b)
        {
            mid=(a+b)>>1;
            if(nums[mid]<=x){
                right=mid;
                a=mid+1;
            }
            else b=mid-1;
        }
        print("%d ", right-left);

    }
}


/*
#include <iostream>
#include <algorithm>
#include <string>
typedef long long int ll;
using namespace std;

#define NM 500005

int N;
int A[NM];

void input() {
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> A[i];
}

int lower_bound(int A[], int L, int R, int X) {
	int ans = R + 1;
	while (L <= R) {
		int mid = (L + R) / 2;
		if (A[mid] >= X) {
			ans = mid;
			R = mid - 1;
		}
		else {
			L = mid + 1;
		}
	}
	return ans;
}

int upper_bound(int A[], int L, int R, int X) {
	int ans = R + 1;
	while (L <= R) {
		int mid = (L + R) / 2;
		if (A[mid] > X) {
			ans = mid;
			R = mid - 1;
		}
		else {
			L = mid + 1;
		}
	}
	return ans;
}

#include <vector>
void pro() {
	sort(A + 1, A + 1 + N);

	int M;
	cin >> M;
	for (int i = 1; i <= M; i++) {
		int X;
		cin >> X;
		cout << upper_bound(A, 1, N, X) - lower_bound(A, 1, N, X) << ' ';
	}
}


int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	input();
	pro();
	return 0;
}
*/