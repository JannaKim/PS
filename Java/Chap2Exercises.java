package Java;
import java.io.*;
import java.util.*;
public class Chap2Exercises 
{
    static public void main(String arv[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //9507092048216 1조 : long
        long regNo;
        String s= br.readLine(); 
        regNo = Long.parseLong(s);

        bw.write(s+"\n",1,5); //offset위치부터 length크기만큼 씀
        bw.write("\n");

   
        //System.out.println('1'+0); // '1': 49
        //System.out.println(true);
        //int system = 3;
        bw.write(3+"\n");
        bw.flush();

        bw.close();

    }
    
}
