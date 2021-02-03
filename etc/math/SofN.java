import java.io.*;
public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long s = Integer.parseInt(br.readLine());
        System.out.println(-1+(long)(Math.sqrt((double)1+8*s)/2));
	}
}

