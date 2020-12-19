package recursion;
import java.io.*;
public class HanoiOrder{
    public static void hanoi(int n, int start, int end, BufferedWriter bw)throws Exception
    {
        if(n==1)
        {
            bw.write(start+" "+end+"\n");
            bw.flush();
            return;           
        }
        int middle = 6- start- end;
        hanoi(n-1,start,middle, bw);
        bw.write(start+" "+end+"\n");
        bw.flush();
        hanoi(n-1,middle,end, bw);


    }

    public static void main(String[] arv) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        int n = Integer.parseInt(s);
        hanoi(n,1,3, bw);
 

    }
}