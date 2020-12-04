package Java.step3;
import java.io.*;

public class ReachN_2741 {
    static public void main(String arv[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        for(int i=1;i<=N;i++)
        {
            bw.write(String.valueOf(i));//출력
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
    
}
