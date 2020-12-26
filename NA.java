import java.io.*;
public class Main{
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void hanoi(int n, int start, int end )throws IOException
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
        bw.write((int)Math.pow(2,n)-1+'\n');
        hanoi(n,1,3);
        bw.flush();
        bw.close();
    }
}