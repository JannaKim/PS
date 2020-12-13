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

        Profile me = new Profile("Minjae Kim", 26, new int[] {159, 43});


        bw.write(me.wei+" " +me.age+" "+me.nation+ "\n");
        bw.flush();
        
    }
}


public class Profile {
    String name;
    int age;
    int H;
    int wei;
    String nation= "Korean";

    public Profile(String name, int age, int[] HW){
    this.name= name; // 파이썬처럼 중복안되네 
    this.age = age;
    H = HW[0];
    wei = HW[1];
    }
}