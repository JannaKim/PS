package Java.step1;
import java.io.*;
import java.util.*;

public class Mul_2588 {
    static public void main(String arv[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int s1 = Integer.parseInt(br.readLine());
        String s2 = br.readLine();
        char[] ch = s2.toCharArray(); // 문자열을 배열화

        /*
        char A = s2.charAt(0);
        char B = s2.charAt(1);
        char C = s2.charAt(2);
        */

        //int _s1 = Integer.parseInt(s1);

        bw.write(s1*(ch[2]-'0')+"\n"); //'0'과 차이나는 만큼: 순수 숫자
        bw.write(s1*(ch[1]-'0')+"\n");
        bw.write(s1*(ch[0]-'0')+"\n");
        
        bw.write(s1*Integer.parseInt(s2)+"\n");
        bw.flush();
        bw.close();
    }
}
