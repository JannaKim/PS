//큰 수 구성하기
package recursion;
import java.util.*;
import java.io.*;

public class PlaceCard5568 {
	
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


    private static int n;
    private static int k;
    private static String[] ls;
    private static HashSet<String> set= new HashSet<String>();
    //static boolean isUsed[];
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        //isUsed = new boolean[n];
        k = Integer.parseInt(br.readLine());
        ls = new String[n];
		for(int i=0; i<n; ++i) {
			ls[i] = br.readLine();
		}
        selection(0,0,0,"");
		bw.write(set.size()+"\n");
		bw.flush();
	}
	
	public static void selection(int floor,int sel,int bitmask,String s)throws IOException {
        if(floor== n+1) // 초과: 재귀 끝냄
            return;
        if(sel==k){ // k개 골랐으니 재귀 끝냄
            set.add(s);
            return;
        }
        for(int i=0;i<n;++i){ //nPk용 포문
            int isUsed= 1<<i & bitmask;
            if(isUsed>0) continue;
            int newbit= (1<<i)| bitmask;
            //if(isUsed[i]) continue;
            //isUsed[i] = true;
            selection(floor+1, sel+1, newbit,s+ls[i]);
            //isUsed[i] = false;
        }
    }
	

}