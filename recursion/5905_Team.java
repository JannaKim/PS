package recursion;
import java.util.Scanner;

public class Main {
	static String mu = "moo";
	static int i = 1;
	
	public static String Moo(int k) {
		if(k == 0) return mu;
		String moo[] = {"m", "o"};
		if(k > 0) {
			mu = mu + moo[0] + moo[1].repeat(i + 2) + mu;
		}
		i++;
		return Moo(k-1);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt();
		sc.close();
		System.out.println(Moo(k));
		
	}

}
