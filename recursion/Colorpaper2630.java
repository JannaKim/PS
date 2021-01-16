import java.util.*;
import java.io.*;
public class Main {
	
	static int blue = 0;
    static int white = 0;
    static int[][] arr; 

	public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        arr= new int[n][n];
		StringTokenizer st;
		for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine()," ");
			for(int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		cnt(arr, 0, 0, n);
		bw.write(white+"\n"+blue);
  		
  		bw.flush();
  		bw.close();
  		br.close();
		

	}
	
	public static void cnt(int[][] arr, int i, int j, int n) {
		
		int sum = 0;
		
		for(int k = i; k < i+n ; k++) {
			for(int h = j; h < j+n; h++) {
				sum += arr[k][h];
			}
		}
				
		if(sum == n*n) {
            blue++;
            return;
		}
		else if(sum == 0) {
            white++;
            return;
		}
		
        n = n/2;
        cnt(arr, i, j, n);
        cnt(arr, i+n, j, n);
        cnt(arr, i, j+n, n);
        cnt(arr, i+n, j+n, n);
		
	}

}
