package Java;
import java.io.*;
import java.util.*;

public class NoW {
    public static void main(String[] arv) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int string;
        int cnt = 0;
        int pre=32;

        while (true){
            string= br.read();
            if (string==32) {//space
                if (pre!=32) {
                    cnt++;
                }

            } else if(string==10){ //enter
                if (pre!=32) {
                    cnt++;
                }
                break;
            }
            pre=string;

        }
        System.out.println(cnt);
    }
}

