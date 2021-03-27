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
// left~right 의 땅을 개발해서 얻을 수 있는 최대 이익!
int solve(int left, int right) {
   cout<<left<<' '<<right<<endl;
   if (dy[left][right] != 0)
      return dy[left][right];
   if (left + 1 == right) { // 가장 작은 문제라면
      return dy[left][right] = max(a[left], a[right]);
   }
   int m = (left + right) / 2;
   // i~m / m+1 ~ j
   
   // 왼쪽 절반을 선택하는 경우
   int select_left = *max_element(a + left, a + m + 1) + solve(m + 1, right);
   // 오른쪽 절반
   int select_right = solve(left, m) + *max_element(a + m + 1, a + right + 1);
   return dy[left][right] = max(select_left, select_right);
}
int main() {
   ios::sync_with_stdio(false); cin.tie(NULL);
   input();
   cout << solve(1, N);
   return 0;
}