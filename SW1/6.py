'''
8
10 10 10 10 1 1 1 1

201


8
1 2 3 4 5 6 7 8

18

8
9 8 7 6 9 8 7 5

25
'''
n= int(input())
#dp[i][j]= i~j를 개발할때 얻는 최대 이익
L=[*map(int, input().split())]

r=0
while 2**r<n: # n= 2^r 인 r 찾기
    r+=1

dp=[[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i]= L[i]

for k in range(1,r+1): # 바텀업으로 dp 다 만들어놓고
    for i in range(0,n-1,2**k):
        #print(i,i+2**k-1, i, i+2**(k-1)-1, i+2**(k-1), i+2**k-1)
        dp[i][i+2**k-1]= max(dp[i][i+2**(k-1)-1], dp[i+2**(k-1)][i+2**k-1])

def td(lo, hi): # 탑다운으로 답 구함
    if hi-lo==1:
        return max(dp[lo][lo], dp[hi][hi])
    m= (lo+hi)//2
    if dp[lo][m]>dp[m+1][hi]:
        #print(f'td({lo},{m})+{dp[m+1][hi]}')
        return td(lo,m)+dp[m+1][hi]
    else:
        #print(f'{dp[lo][m]}+td({m+1},{hi})')
        return dp[lo][m]+td(m+1,hi)

print(td(0,n-1))


'''
#include <iostream>
#include <algorithm>
#include <string>
#define NM 10
#define INF 0x7fffffff
#define vi vector<int>
FILE* in = stdin, * out = stdout;
using namespace std;
#include <unordered_map>
int N;
int a[1030];
int dy[1030][1030];
void input() {
   cin >> N;
   for (int i = 1; i <= N; i++) cin >> a[i];
}
void pro() {
   for (int i = 1; i <= N; i += 2)
      dy[i][i + 1] = max(a[i], a[i + 1]);
   for (int size = 4; size <= N; size *= 2) {
      for (int left = 1; left <= N; left += size) {
         // left ~ left + size - 1
         int right = left + size - 1;
         int m = (left + right) / 2;
         // 왼쪽 절반을 선택하는 경우
         int select_left = *max_element(a + left, a + m + 1) + dy[m + 1][right];
         // 오른쪽 절반
         int select_right = dy[left][m] + *max_element(a + m + 1, a + right + 1);
         dy[left][right] = max(select_left, select_right);
      }
   }
   cout << dy[1][N];
}
int main() {
   ios::sync_with_stdio(false); cin.tie(NULL);
   input();
   pro();
   return 0;
}
'''