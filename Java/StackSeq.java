import java.io.*;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=0, top=0, nxt=0, cur=0;
        n = Integer.parseInt(br.readLine());
        int stack[] = new int[n];
        StringBuilder sb = new StringBuilder();
        while (n-- >0)
        {
            nxt = Integer.parseInt(br.readLine());
            if (nxt > cur) {
                while (nxt > cur) {
                    stack[top++] = ++cur;
                    sb.append("+\n");
                }
            } else if (stack[top - 1] != nxt) {
                System.out.print("NO");
                return;
            }
            top--;
            sb.append("-\n");
            if (nxt > cur) cur = nxt;
        }
        System.out.println(sb);

    }
}

