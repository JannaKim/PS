package recursion;
import java.io.*;
import java.math.BigInteger;
public class HanoiOrder{
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static void hanoi(int n, char start, char end )throws IOException
    {
        if(n==1)
        {
            bw.write(start+" "+end+"\n");
            return;           
        }
        int a=start-'0';
        int b=end-'0';

        int middle = 6- a- b;
        char mid= (char)(middle+'0');
        hanoi(n-1,start,mid);
        bw.write(start+" "+end+"\n");
        hanoi(n-1,mid,end);

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
        hanoi(n,'1','3');
        }
        bw.close();
    }
}