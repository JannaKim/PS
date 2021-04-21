package Java;
import java.io.*;
import java.util.*;

public class NoW {
    public static void main(String[] arv) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int word;
        int[] hs= new int[26];
        String in = br.readLine();
        int n = in.length();
        for (int i = 0; i < n; i++) {
            word = in.charAt(i);
            if (word>=97){
                hs[word-97]++;
            }
            else{
                hs[word-65]++;
            }

        }
        int mx=0;
        int d=0;
        int ans=0;
        for (int i = 0; i < 26; i++) {
            if (hs[i]>mx){
                mx=hs[i];
                ans=i;
                d=0;
            }
            else if (hs[i]==mx){
                d++;
            }
        }
        if(d>0){
            System.out.println('?');
        }
        else{
            //ans=65;
            System.out.printf("%c",65+ans);
        }

    }
}//array length with no (), String with ()