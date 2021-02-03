import java.util.Scanner;
import java.util.Arrays;

public class Coordinate_Sort_11651 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		int arr[][] = new int[size][2];
		
		for(int i = 0; i < size; i++) {
			arr[i][0] = sc.nextInt();
			arr[i][1] = sc.nextInt();
		}
	
		Arrays.sort(arr, (o1, o2) -> {
			if(o1[1] == o2[1]) {
				return Integer.compare(o1[0],  o2[0]);}
			else {
				return Integer.compare(o1[1], o2[1]);
			}
		});
		
		for(int i = 0; i < size; i++) {
			System.out.print(arr[i][0] + " " + arr[i][1]);
			System.out.println();
		}
	}
}