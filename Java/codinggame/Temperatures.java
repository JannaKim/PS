package Java.codinggame;

import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Temperatures{

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        int ans=5527;
        for (int i = 0; i < n; i++) {
            int t = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526
            int abs_t = Math.abs(t);
            int abs_ans=Math.abs(ans);
            
            if(abs_t==abs_ans){
                if(t<0 && ans<0) ans = t;
                else ans = abs_t;

                //if(t>0) ans = abs_t;
            }
            if(abs_t<abs_ans) ans=t;  
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        if(ans==5527) System.out.println(0);
        else System.out.printf("%d%n",ans);
    }
}
