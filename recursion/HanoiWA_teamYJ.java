package recursion;
    

import java.io.*;

public class HanoiWA_teamYJ  {
	
	public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		bw.write(String.valueOf((int)Math.pow(2,N)-1)+'\n');
        bw.flush();
        hanoi(N, '1', '2', '3');
	}
	
	public static void hanoi(int N, char start, char mid, char end) throws IOException {
		if(N==1) {
			bw.write(start+" "+end+"\n");
			bw.flush();
			return;
		}
		else {
			hanoi(N-1, start, end, mid);
			bw.write(start+" "+end+"\n");
			hanoi(N-1, mid, start, end);
		}
	}

}