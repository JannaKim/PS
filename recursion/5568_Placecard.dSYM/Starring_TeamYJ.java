package recursion;

import java.io.*;

public class Starring_TeamYJ{
	
	private static int N;
	private static String[][] arr;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());
		int len = 4*N-3;
		
		arr = new String[len][len];
		for(int i=0; i<len; i++) {
			for(int j=0; j<len; j++) {
				arr[i][j] = " ";
			}
		}
		
		square(N, 0, 0);
		
		for(int i=0; i<len; i++) {
			for(int j=0; j<len; j++) {
				bw.write(arr[i][j]);
			}
			bw.write("\n");
		}
		bw.close();
	}

	public static void draw(int len, int row, int col) {
		for(int i=0; i<len; i++) {
			if(i==0 || i==len-1) {
				for(int j=0; j<len; j++) {
					arr[row+i][col+j] = "*";
				}
			}
			else {
				arr[row+i][col] = "*";
				arr[row+i][col+len-1] = "*";
			}
		}
	}
	
	public static void square(int n, int row, int col) {
		draw(n*4-3, row, col);
		if(n==1) return;
		else square(n-1, row+2, col+2);
	}

}