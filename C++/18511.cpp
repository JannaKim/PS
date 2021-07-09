#include<iostream>
#include<algorithm>
#include<string>
#include<algorithm>
using namespace std;
int N, K;
int arr[3];
int ans;
void DFS(string num, int cnt) {
	if (cnt == K) {
		if (stoi(num) <= N) {
			ans = max(ans, stoi(num));
		}
		return;
	}
	for (int i = 0; i < K; i++) {
		DFS(num + to_string(arr[i]), cnt + 1);
		DFS(num + '0', cnt + 1); //한자리가 나오는 경우
		
	}
}
int main() {
	cin >> N >> K;
	for (int i = 0; i < K; i++) {
		cin >> arr[i];
	}
	DFS("",0);
	cout << ans;
}
