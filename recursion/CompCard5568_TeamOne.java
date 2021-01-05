import java.util.*;

public class PutSomeCard5568_TeamOne {
	static HashSet<String> a = new HashSet<String>();
	
	public static void Shuffled(String arr[], int k, int n) {
		if (k == 0) return;
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr.length; j++) {
				if(i == j) continue;
				a.add(arr[i] + arr[j]);
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		String arr[] = new String[n];
		
		for(int i = 0; i < n; i++) 
			arr[i] = sc.next();
		
		Shuffled(arr, k, 0);
		Iterator it = a.iterator();
		
		while(it.hasNext())
			System.out.println(it.next());
	}
}