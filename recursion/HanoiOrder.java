package recursion;
import java.io.*;
import java.math.BigInteger;
public class HanoiOrder{
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static void hanoi(int n, int start, int end )throws IOException
    {
        if(n==1)
        {
            bw.write(start+" "+end+"\n");
            return;           
        }
        int middle = 6- start- end;
        hanoi(n-1,start,middle);
        bw.write(start+" "+end+"\n");
        hanoi(n-1,middle,end);

    }

    public static void main(String[] arv) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        BigInteger bi= BigInteger.ONE;
        for(int i=0; i<n;i++){
            bi=bi.multiply(BigInteger.valueOf(2L));
        } 
        bi= bi.subtract(BigInteger.valueOf(1L));
        bw.write(bi.toString()+'\n'); //?
        if(n<=20){
        hanoi(n,1,3);
        }
        bw.close();
    }
}