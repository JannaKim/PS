package DP;
import java.util.Scanner;
public class Main {
   public static void Cantor(int size) {
      if(size == 1) {
   System.out.print("-");
   } else { 
      Cantor(size / 3);
      for(int i = 0; i < size / 3; i++) {
         System.out.print(" ");
         }
      Cantor(size / 3);
      }
   }
   
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      while(sc.hasNextInt()) {
         int N = sc.nextInt();
         Cantor((int) Math.pow(3, N));
         System.out.println();
      }
   }
}