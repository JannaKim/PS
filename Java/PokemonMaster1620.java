import java.io.*;
import java.util.*;


public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<String, String> pokedex = new HashMap<String, String>(n * 2);
        for (int i = 1; i < n + 1; ++i) {
            String name = br.readLine();
            pokedex.put(name, Integer.toString(i));
            pokedex.put(Integer.toString(i), name);

        }
        for (int i = 1; i < m + 1; ++i) {
            System.out.println(pokedex.get(br.readLine()));
        }
    }
    }
