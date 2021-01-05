//큰 수 구성하기
package recursion;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.*;

public class CompBigNumTeamOne18511 {
	
	private static int[] list;
	private static int N;
	private static int K;
	private static int ans;
	private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		list = new int[K];
		for(int i=0; i<K; i++) {
			list[i] = Integer.parseInt(st.nextToken());
		}
        Arrays.sort(list);
        recursive(0,1);
		bw.write(ans+"\n");
		bw.flush();
	}
	
	public static void recursive(int num, int ten)throws IOException {
		if(num<1000){
			bw.write(num+"\n");
			bw.flush();
		}
		if(num>N) return;

        ans = Math.max(ans, num);
        for(int i=K-1; i >= 0; i--){
            recursive(num + ten * list[i], ten*10);
        }
	}

}