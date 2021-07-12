#include<iostream>
#include<algorithm>
#include<string>
#include<algorithm>
using namespace std;
int N, K;
int arr[5];
int ans = 0;
void DFS(string num, int cnt) {
	if (cnt == K) {
		if (stoi(num) <= N) {
			ans = max(ans, stoi(num));
		}
		return;
	}
	for (int i = 0; i < K; i++) {
		DFS(num + to_string(arr[i]), cnt + 1);
		DFS('0' + num, cnt + 1); //한자리가 나오는 경우
		
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
