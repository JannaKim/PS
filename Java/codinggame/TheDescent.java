package Java.codinggame;

import java.util.*;
import java.io.*;
import java.math.*;

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/
class TheDescent{

    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        // game loop
        while (true) {
            int mx=0;
            int idx=0;
            String[] s  = br.readLine().split(" "); 
            for (int i = 0; i < 8; i++) {
                int mountainH = Integer.parseInt(s[i]);
                if(mx<mountainH)
                {
                    mx = mountainH;
                    idx=i;
                }
                // represents the height of one mountain.
            }

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");

            bw.write(idx+0+"\n");// The index of the mountain to fire on.
            bw.flush();

        }
    }
}