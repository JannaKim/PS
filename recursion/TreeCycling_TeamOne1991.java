import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node {
	int index;
	Node parent;
	Node leftchild;
	Node rightchild;

	public Node(int index) {
		this.index = index;
	}
}

public class Main {
	static Node[] node;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		node = new Node[N];

		for (int i = 0; i < N; i++) {
			node[i] = new Node(i);
		}
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			// 0 -> index 0번째
			// -'A' -> A는 숫자 0으로 들어간다.
			int parent = st.nextToken().charAt(0) - 'A';
			int left = st.nextToken().charAt(0) - 'A';
			int right = st.nextToken().charAt(0) - 'A';

			if (left >= 0)
				node[parent].leftchild = node[left];
			if (right >= 0)
				node[parent].rightchild = node[right];
		}
		br.close();
		preOrder(0);
		System.out.println();
		inOrder(0);
		System.out.println();
		PostOrder(0);
	}

	private static void PostOrder(int tree) {
		// 왼쪽 노드 확인
		if (node[tree].leftchild != null)
			PostOrder(node[tree].leftchild.index);
		
		// 오른쪽 노드 확인
		if (node[tree].rightchild != null)
			PostOrder(node[tree].rightchild.index);
		
		//자신 노드 확인
		System.out.print((char)(node[tree].index+'A'));
	}
	
	private static void inOrder(int tree) {
		// 왼쪽 노드 확인
		if (node[tree].leftchild != null)
			inOrder(node[tree].leftchild.index);
		
		//자신 노드 확인
		System.out.print((char)(node[tree].index+'A'));
		
		// 오른쪽 노드 확인
		if (node[tree].rightchild != null)
			inOrder(node[tree].rightchild.index);
		
	}
	
	private static void preOrder(int tree) {
		//자신 노드 확인
		System.out.print((char)(node[tree].index+'A'));
		
		// 왼쪽 노드 확인
		if (node[tree].leftchild != null)
			preOrder(node[tree].leftchild.index);
		
		// 오른쪽 노드 확인
		if (node[tree].rightchild != null)
			preOrder(node[tree].rightchild.index);
		
	}

}