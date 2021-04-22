from collections import deque
N, K = map(int, input().split())
q=deque()
for i in range(1,N+1):
    q.append(i)

ans=[]
while q:
    for _ in range(K-1):
        temp = q.popleft()
        q.append(temp)n
    ans.append(str(q.popleft()))

print("<",end='')
print(', '.join(ans), end='')
print(">")


    

'''
#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int N, K;
	cin >> N >> K;
	queue<int> qu;
	for (int i = 1; i <= N; ++i)
	{
		qu.push(i);
	}
	cout << "<";
	while (qu.size() > 1)
	{
		for (int i = 0; i < K-1; ++i)
		{
			qu.push(qu.front());
			qu.pop();
		}
		cout << qu.front() << ", ";
		qu.pop();
	}
	cout << qu.front() << ">";

	return 0;
}
'''