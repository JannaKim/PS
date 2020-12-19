package programmers;
import java.io.*;
import java.lang.*; //?

public class Keypad {
    static String solution(int[] numbers, String hand) {
        String answer = "";
        int L =10;
        int R =12;
        for(int i:numbers)
        {
            if(i==0)i=11;
    
            if(i==2|| i==5|| i==8|| i==11)
            {
                int[] locL={(L-1)/3, (L-1)%3};
                int[] locR={(R-1)/3, (R-1)%3};
                int[] locI={(i-1)/3, (i-1)%3};

                int dLI= Math.abs(locL[0]-locI[0])+ Math.abs(locL[1]-locI[1]);
                int dRI= Math.abs(locR[0]-locI[0])+ Math.abs(locR[1]-locI[1]);

                if(dLI< dRI){ L=i; answer+='L';}
                else if(dLI> dRI){ R=i; answer+='R';}
                else
                {
                    if(hand=="right"){ R=i; answer+='R';}
                    else { L=i; answer+='L';}
                }
            }
            else
            {
                if((i-1)%3==0) { L=i; answer+='L';}
                else { R=i; answer+='R';}
            }
    
    
        }
        return answer;
    }
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new 
        InputStreamReader(System.in));

        
        BufferedWriter bw = new BufferedWriter(new
        OutputStreamWriter(System.out));
        int a= 0%3;
        bw.write(a+'\n');
        bw.flush();
    }

}

/*
public class Solution {

}*/