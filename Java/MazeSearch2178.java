package Java;
import java.io.*;
import java.util.*;

public class MazeSearch2178 {
    static int[] Dy= {0,0,1,-1};
    static int[] Dx= {1,-1,0,0};
    public static void main(String[] arv) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] maze= new int[n][m];

        for (int i=0; i<n; i++){
            String in= br.readLine();
            for(int j=0; j<m; j++)
            {
                maze[i][j]= in.charAt(j)-'0';
            }
        }

        boolean [][] visit= new boolean[n][m]; // initialized: false
        Deque<int []> q= new ArrayDeque<>();
        q.offer(new int[] {0,0});
        visit[0][0]= true;
        while(!q.isEmpty()) {
            int[] cur= q.poll();
            //System.out.println(cur[0]+ " " +cur[1]);
            for(int dir =0; dir<4; dir++)
            {
                int nx= cur[0]+Dx[dir];
                int ny= cur[1]+Dy[dir];
                if(0> nx || nx>=n || 0>ny || ny>=m) continue;
                if(maze[nx][ny]==1 && !visit[nx][ny]){
                    q.offer(new int[] {nx,ny});
                    visit[nx][ny]=true;
                    maze[nx][ny]= maze[cur[0]][cur[1]]+1;
                }

            }
        }
        System.out.println(maze[n-1][m-1]);




    }

}
