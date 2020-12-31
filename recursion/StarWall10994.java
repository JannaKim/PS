package recursion;
import java.util.*;
import java.io.*;
public class StarWall10994 {
    static int widest;
    static String[][] pic = new String[400][400];

    

    static void star(int x, int y, int n)
    {
        if(n==0) return;
        int side= 4*n-3;
        for(int i=0;i<side;++i)
        {
            pic[x+i][y]="*"; //왼벽
            pic[x][y+i]="*"; //지붕
            pic[x+side-1][y+i]="*";//바닥
            pic[x+i][y+side-1]="*";
        }
        star(x+2,y+2,n-1);
    }
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        widest= 4*n-3;
        

        for(int i=0;i<widest;++i)
        {
            for(int j=0;j<widest;++j)
            {
                pic[i][j]= " ";
            }
        }

        star(0,0,n);
        for(int i=0;i<widest;++i)
        {
            for(int j=0;j<widest;++j)
            {
                bw.write(pic[i][j]+"");
            }
            bw.write("\n");
        }
        bw.close();
    }
    
}
