package recursion;
import java.util.Scanner;
// 등차수열 일반항 : An = A1 + (n - 1)d
// 여기서의 일반항 An = 4n - 3이다.

public class TeamOne_Stars10994 {
	static String a[][];
	
	public static void Stars(int n, int len) {
		for(int i = n; i < len; i++) {
			a[n][i] = "*"; //지붕
			a[i][n] = "*"; //좌벽
			a[i][len-1] = "*"; //우벽
			a[len-1][i] = "*"; //바닥
		}
		
		if(len == 1) return;
		Stars(n+2, len-2);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int size = 4 * n - 3;
		a = new String[size][size];
		
		for(int i = 0; i < size - 1; i++)
			for(int j = 0; j < size - 1; j++) a[i][j] = " ";
			
		Stars(0, size);
		
		for(int i = 0; i < size; i++) {
			for(int j = 0; j < size; j++) {
				System.out.print(a[i][j]);
			}
			System.out.println();
		}
		
		sc.close();
	}
}