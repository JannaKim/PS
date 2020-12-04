package Java.step1;
import java.util.*;
import java.io.*;

public class AplusB_1000 {
    public static void main(String args[]) throws Exception
    {
        int a, b;
        //Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new 
        InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");
        //a = sc.nextInt();
        //b = sc.nextInt();
        a = Integer.parseInt(s[0]);
        b = Integer.parseInt(s[1]);
        

        /*
        String input;
        input = sc.nextLine();
        a = Integer.parseInt(input);
        input = sc.nextLine();
        b = Integer.parseInt(input);
        */

        BufferedWriter bw = new BufferedWriter(new
        OutputStreamWriter(System.out));

        //System.out.println(a+b);
        bw.write(a+b+"\n");
        bw.flush();
    }
    
}
