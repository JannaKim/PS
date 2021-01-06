package recursion;
import java.util.Scanner;

public class MultipleOf3_1769_TeamOne {
	static int count = 0;
	public static int Multi(int X) {
		int Y = 0;
		while(X > 0) {
			Y += X % 10;
			X /= 10;
		}
		count++;

		if(Y > 9) {
			X = Y;
			return Multi(X);
		} else { 
			return Y;
		}

	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int X = sc.nextInt();
		sc.close();
		if(Multi(X) % 3 == 0) {
			System.out.println(count);
			System.out.println("YES");
		} else {
			System.out.println(count);
			System.out.println("NO");
		}
	}

}