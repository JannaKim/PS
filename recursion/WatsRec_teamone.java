package recursion;
import java.io.*;

public class WatsRec_teamone {
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static int i = 0;
	public static String Recursion(int repeat) throws IOException {

        if(repeat == 0) return "-".repeat(4*i) + "\"재귀함수가 뭔가요?\"" + "\n" + "-".repeat(4*i) + "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
        bw.write("-".repeat(4*i) + "\"재귀함수가 뭔가요?\"");
        bw.write("-".repeat(4*i) + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
        bw.write("-".repeat(4*i) + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
        bw.write("-".repeat(4*i) + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
        i++;
        return Recursion(repeat-1);
	}
	
	public static String Answer(int repeat)  throws IOException {
		if(i >= 0) {
			bw.write("-".repeat(4*i) + "라고 답변하였지.");
			i--;
			return Answer(repeat - 1);
		} else { return ""; }
	}

	public static void main(String[] args)  throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int repeat = Integer.parseInt(br.readLine());
        bw.write("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
		bw.write(Recursion(repeat));
        bw.write(Answer(repeat));
        bw.close();
	}

}
