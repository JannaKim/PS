package CLASS;

import java.io.*;
import java.util.*;




public class ClassEx{
    public static void main(String[] arv) throws IOException
    {
        BufferedReader br = new BufferedReader(new 
        InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new 
        OutputStreamWriter(System.out));

        JannaProfile hi = new JannaProfile();


        bw.write(hi.H+"\n");
        bw.flush();
        
    }
}


public class JannaProfile {
    String name="Minjae Kim";
    int H = 159;
    int wei = 43;
}