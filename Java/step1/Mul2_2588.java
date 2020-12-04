package Java.step1;
import java.io.*;

public class Mul2_2588 {
    static public void main(String[] arv) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int num1 = Integer.parseInt(br.readLine());
        String s = br.readLine();
        /*
        char[] c = s.toCharArray();
        for(int i=0;i<c.length;i++)
        {
            bw.write(num1*(c[i]-'0')+"\n");
        }
        */
        for(int i=s.length()-1;i>=0;i--)
        {
            bw.write(num1*(s.charAt(i)-'0')+"\n");
        }
        bw.write(num1*Integer.parseInt(s)+"\n");
        bw.flush();
        bw.close();

    }
    
}
