N, K = map(int, input().split())
pic=[]
for _ in range(N):
    pic.append(input()+' ')

for i in range(N):
    for _ in range(K):
        for j in range(0,2*N,2):
            print(pic[i][j:j+2]*K, end='')
        print()
'''
n, k = map(int, input().split())
d = []
for i in range(n):
    v = input().split()
    vv = [v[i // k] for i in range(n * k)]
    for j in range(k):
        d.append(vv)
for v in d:
    print(' '.join(v))
'''


'''
#include <cstdio>

int main() {
	int n, k, a[10][10];
	scanf("%d%d", &n, &k);
	for (int i = 0 ; i < n ; i++) for (int j = 0 ; j < n ; j++) scanf("%d", &a[i][j]);
	for (int i = 0 ; i < n * k ; i++) {
		for (int j = 0 ; j < n * k ; j++) {
			printf("%d ", a[i/k][j/k]);
		}
		printf("\n");
	}
}


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			for (int y = 0; y < k; y++) {
				for (int j = 0; j < n; j++) {
					for (int x = 0; x < k; x++) {
						sb.append(arr[i][j]).append(" ");	
					}
				}
				sb.append(System.lineSeparator());
			}
		}
		
		System.out.println(sb.toString());
	}

}

'''