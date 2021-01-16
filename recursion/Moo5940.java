import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        while(true)
        {
            long seq= 0;
            long i=0;
            while(true)
            {
                long next=seq*2+3+i;
                if(next>=n) break;
                seq= seq*2+3+i;
                i+=1;
            }
            n-=seq;
            if(n<=3+i)
            {
                if(n==1){ bw.write('m'); bw.close(); break;}
                else{ bw.write('o'); bw.close(); break;}
            }
            n-= 3+i;
        }
    }
}