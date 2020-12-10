package Java;
import java.io.*;
import java.util.*;
import java.lang.Math;

public class MinMax_10818 {
    public static void main(String[] arv) throws IOException
    {
        BufferedReader br = new BufferedReader(new
        InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new
        OutputStreamWriter(System.out));

        String n = br.readLine();
        int N = Integer.parseInt(n);
        String[] input = br.readLine().split(" ");

        long mx=-1000_000L-1L;
        long mn = 1000_000+1;


        //int[] numbers = new int[N];
        for(int i=0; i<N; ++i)
        {
            //numbers[i] = Integer.parseInt(input[i]);
            int x = Integer.parseInt(input[i]);
            mx = Math.max(mx, x);
            mn = Math.min(mn, x);
        }

        bw.write(mn+" "+mx+"\n");
        bw.flush();



    }
    
}
