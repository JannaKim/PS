n= int(input())
*L, =map(int, input().split())
L.sort()

if sum(L)!=(n-1)*n//2:
    print(-1)
    exit()
node= list(range(n))
indegree= [0]*n
for idx,el in enumerate(L):
    indegree[idx]=n-1-el

#print(indegree)
cur=0
for j in range(n-1,-1,-1):
    for i in range(n): # 꼴찌순으로 이겼을 보장이 없지 않나
        if i==j: # 자기 자신은 지나침
            continue
        if indegree[i]:
            indegree[i]-=1
            L[j]-=1
        if L[j]==0:
            break
    indegree.sort(reverse=True)
    if L[j]!=0:
        #print(j,L[j],indegree)
        print(-1)
        exit()
#print(indegree)
if sum(indegree)==0 and sum(L)==0:
    print(1)
else:
    print(-1)


'''
#include <cstdio>
#include <algorithm>
#define MAX_N 10000
using namespace std;
int c[MAX_N + 1], n, f;
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        scanf("%d", &c[i]);
    sort(c + 1, c + 1 + n);
    for (int i = 1; i <= n; i++) {
        if (c[i] > n - i || c[i] < 0) {
            f = 1;
            break;
        }
        for (int j = 0; j < n - c[i] - i; j++)
            c[n - j]--;
        sort(c + i + 1, c + 1 + n);
    }
    printf("%d\n", f ? -1 : 1);
    return 0;
}
'''