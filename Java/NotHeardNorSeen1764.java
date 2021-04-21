import java.io.*;
import java.util.*;


public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<String, boolean> ls = new HashMap<String, boolean>(n+m);
        for (int i = 0; i < n; ++i) {
            String name = br.readLine();
            ls.put(name, false);
        }
        for (int i = 0; i < m; ++i) {
            String name = br.readLine();
        }
    }

}
