import java.io.*;
import java.util.*;

public class Main {
	
	public static Map<String, String[]> map = new HashMap<>();
	//Object

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		
		for(int i=0; i<N; i++) {
			String[] node = br.readLine().split(" ");
			map.put(node[0], new String[] {node[1], node[2]});
		}
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(preOrder("A")+"\n");
        bw.write(inOrder("A")+"\n");
        bw.write(postOrder("A")+"\n");
        bw.close();
		
	}
	
	public static String preOrder(String c) {
        if(c.equals(".")) return"";
		String[] node = map.get(c);
        return c+preOrder(node[0])+preOrder(node[1]);
	}
	
	public static String inOrder(String c) {
		if(c.equals(".")) return"";
		String[] node = map.get(c);
		return inOrder(node[0])+c+inOrder(node[1]);
	}
	
	public static String postOrder(String c) {
		if(c.equals(".")) return"";
		String[] node = map.get(c);
		return postOrder(node[0])+postOrder(node[1])+c;

	}
}
