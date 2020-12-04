package Java;
import java.util.*;

import java.io.*;
public class Chapter2Finished {
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s = br.readLine();
        float a = Float.parseFloat(s);
        boolean checked = false;
        //System.out.printf("%f%n",a);
        bw.write(a+"\n");
        bw.write(checked+"\n");

        char c = 65;
        char d = 'A';
        bw.write(c+"\n");
        bw.write(d+"\n");
        bw.flush();

        //2의 보수 계산 = 1의 보수+1

        //JVM의 피연산자 스택(operand stack)이 피연산자를 4byte 단위로 저장하기 때문에 
        // 크기가 4byte보다 작은 자료형(byte, short)의 값을 계산할 때는 4byte로 변환하여 연산을 수행하므로
        // 정수형 변수를 선언할 때 int타입으로 하는 게 더 효율적이다.

        //signed short = 3만
        //signed int = 20억
        //



    }
    
}
