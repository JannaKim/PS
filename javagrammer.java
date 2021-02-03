import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.*;
import java.math.*;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
			//Scanner sc = new Scanner(System.in);
			//int a = sc.nextInt();
			//int b = sc.nextInt();
			//String b = sc.next();
			//int c = sc.nextInt();
			//print();
			//sumTwo(a,b);
			//diffTwo(a,b);
			//print2();
			//print3();
			//print4();
			//print5();
			//multiTwo(a,b);
			//divideTwo(a,b);
			//divideTwoQuotient(a,b);
			//divideTwoRemainder(a,b);
			//calThree(a,b,c);
			//calMinSet(a);
			//print6(a);			
			//print7(a);
			//print8(a);
			//print9(a);
			//print10(a);
			//print11(a);
			//print12(a);
			//calDate(a,b);
			//print13(a);
			//sumLine(a,b);
			//print14(b);
			//print15(a);
			//print16(a,b,c);
			//print17(a,b,sc);
			//print18();
			//calAvg();
			//calAvg2();
			//calHansu();
			//print19();
			//calWord();
			//calRadix();
			//calPoint();
			//print20();
			//calAvg3();
			//printAscii();
			//printAlpha();
			//printReChar();
			//countChar();
			//calBigger();
			//groupWord();
			//dialTime();
			//calChroAlpa();
			//minDistance();
			//calDistance();
			//calDistance2();
			//CalRoomNum();
			//CalApartCount();
			//CalNeedSet();
			//CalSetOrder();
			//NOrdering();
			//NOrdering2();
			//NOrdering3();
			//Statistics();
			//RadixSorting();
			//WordSorting();
			//Decimal();
			//Decimal2();
			//Decimal3();
			//Decimal4();
			//Decimal5();
			//Stack();
			//Stack2();
			//Stack3();
			//Stack4(); 
			//Queue();
			//Queue2();
			//Queue3();
			//Queue4();
			//Queue5();
			//PriotyQueue();
			//Deck();
			//Deck2();
			//Deck3();
			//Fibo();
			//Fibo2();
			//Fibo3();
			//Combine();
			//Combine2();
			//Combine3();
			//Factorial();
			//Factorial2();
			//Combine4();
			//Combine5();
			//Combine6();
			//minCostRGB();
			//maxCostTriangle();
			//maxCostStair();
			//minCostNumOne();
			minCostConstruct();
	}
	
	public static void sumTwo(int a, int b){
		System.out.println(a+b);
	}
	
	public static void diffTwo(int a, int b){
		System.out.println(a-b);
	}
	
	public static void multiTwo(int a, int b){
		System.out.println(a*b);
	}
	
	public static void divideTwo(int a, int b){
		System.out.println((double) a / (double) b);
	}
	
	public static void divideTwoQuotient(int a, int b){
		System.out.println(a/b);
	}
	
	public static void divideTwoRemainder(int a, int b){
		System.out.println(a%b);
	}
	
	public static void calThree(int a, int b, int c){
		System.out.println((a+b)%c);
		System.out.println(((a%c)+(b%c))%c);
		System.out.println((a*b)%c);
		System.out.println(((a%c)*(b%c))%c);
	}
	
	public static void calMinSet(int a){
		int x = 0; //5
		int y = 0; //3
		for(int i = (a/5); i >= 0; i--){
			if((a-(5*i))%3 == 0){
				x=i;
				y=(a-(5*i))/3;
				System.out.println(x+y);
				break;
			}
		}
		if(x == 0 && y == 0){
			System.out.println("-1");
		}
	}
	
	public static void calDate(int a, int b){
		int arr[]={31,28,31,30,31,30,31,31,30,31,30,31};
		String sarr[] = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
		int sum = 0;
		for(int i=0; i<a-1; i++){
			sum+=arr[i];
		}
		sum+=b;
		System.out.println(sarr[sum%7]);
	}
	
	public static void sumLine(int a, String b){
		int sum = 0;
		
		for(int i=0; i<a; i++){
			sum += (int)b.charAt(i)-48;
		}
		System.out.println(sum);
	}
	
	public static void print(){
		System.out.println("Hello World!");
	}
	
	public static void print2(){
		System.out.println("3");
		System.out.println("yjc034");
	}
	
	public static void print3(){
		System.out.println("|\\_/|");
		System.out.println("|q p|   /}");
		System.out.println("( 0 )\"\"\"\\");
		System.out.println("|\"^\"`    |");
		System.out.println("||_/=\\\\__|");
	}
	
	public static void print4(){
		System.out.println("강한친구 대한육군");
		System.out.println("강한친구 대한육군");
	}
	
	public static void print5() throws IOException{ //파일 입출력 ( 표준 리다이렉션 ) 을 이용하여 출력결과가 올바르면 정답.
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		while((s=in.readLine()) != null){
			System.out.println(s);
		}
		in.close();
	}
	
	public static void print6(int a){
		for(int i=1; i<=a; i++){
			System.out.println(i);
		}
	}
	
	public static void print7(int a){
		for(int i=a; i>0; i--){
			System.out.println(i);
		}
	}
	
	public static void print8(int a){
		for(int i=1; i<10; i++){
			System.out.println(a+" * "+i+" = "+a*i);
		}
	}
	
	public static void print9(int a){
		for(int i=1; i<=a; i++){
			for(int j=a-i; j<a; j++){
				System.out.print("*");
			}
			System.out.print("\n");
		}
	}
	
	public static void print10(int a){
		for(int i=1; i<=a; i++){
			for(int j=0; j<a-i; j++){
				System.out.print(" ");
			}
			for(int j=a-i; j<a; j++){
				System.out.print("*");
			}
			System.out.print("\n");
		}
	}
	
	public static void print11(int a){
		for(int i=1; i<=a; i++){
			for(int j=i; j<=a; j++){
				System.out.print("*");
			}
			System.out.print("\n");
		}
	}
	
	public static void print12(int a){
		for(int i=1; i<=a; i++){
			for(int j=1; j<i; j++){
				System.out.print(" ");
			}
			for(int j=i; j<=a; j++){
				System.out.print("*");
			}
			System.out.print("\n");
		}
	}
	
	public static void print13(int a){
		int sum= 0;
		for(int i=1; i<=a; i++){
			sum += i;
		}
		System.out.println(sum);
	}
	
	public static void print14(String a){
		for(int i =0; i<a.length(); i++){
			System.out.print(a.charAt(i));
			if(i%10 == 9)
				System.out.print("\n");
		}
	}

	public static void print15(int a){
		if(a>=90)
			System.out.println("A");
		else if(a>=80)
			System.out.println("B");
		else if(a>=70)
			System.out.println("C");
		else if(a>=60)
			System.out.println("D");
		else
			System.out.println("F");
	}
	
	public static void print16(int a, int b, int c){
		int temp =0;
		if(a>b){
			temp=b;
			b=a;
			a=temp;
		}
		if(a>c){
			temp=c;
			c=a;
			a=temp;
		}
		if(b>c){
			temp=c;
			c=b;
			b=temp;
		}
		System.out.println(b);
	}
	
	public static void print17(int a, int b, Scanner sc){
		for(int i=0; i<a; i++){
			int temp=sc.nextInt();
			if(temp<b){
				System.out.print(temp);
				System.out.print(" ");
			}
		}
	}
	
	public static void print18() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(in.readLine());
		int sum = 0;
		int num = 0;
		for(int i=0; i<a; i++){
			StringTokenizer st = new StringTokenizer(in.readLine());
			num = st.countTokens();
			for(int j=0; j<num; j++){
				sum += Integer.parseInt(st.nextToken());
			}
			System.out.println(sum);
			sum=0;
		}
		in.close();
	}
	
	public static void calAvg() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(in.readLine());
		int num = 0;
		int M = 0;
		double sum = 0;
		double avg = 0;
		
		int arr[] = new int[a];
		double arr2[] = new double[a];
		
		StringTokenizer st = new StringTokenizer(in.readLine());
		num = st.countTokens();
		for(int j=0; j<num; j++){
			arr[j] = Integer.parseInt(st.nextToken());
			if(M < arr[j])
				M = arr[j];
		}
		for(int j=0; j<num; j++){
			arr2[j]= Math.round(arr[j]/(double)M*10000)/(100.0);
			sum += arr2[j];
		}
		avg = sum/a;
		
		System.out.format("%.2f",avg);	
	}
	
	public static void calAvg2() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int C = Integer.parseInt(in.readLine());
		int sum = 0;
		double avg = 0;
		int cnt = 0;
		
		for(int i=0; i<C; i++){
			StringTokenizer st = new StringTokenizer(in.readLine());
			sum = 0;
			cnt = 0;
			avg = 0;
			
			int x = Integer.parseInt(st.nextToken());
			int arr[] = new int[x];
			
			for( int j=0; j<x; j++){
				arr[j]=Integer.parseInt(st.nextToken());
				sum+=arr[j];
			}
			avg = sum/(double)x;
			for( int j=0; j<x; j++){
				if(arr[j]>avg)
					cnt+=1;
			}

			System.out.format("%.3f",Math.round(cnt/(double)x*100000)/(1000.0));
			System.out.println("%");
		}
		in.close();
	}
	
	public static void calHansu() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int diffVal =0;
		int cnt=0;
		int temp = 0;
		
		for(int i=1; i<=N; i++){
			if(i<100){
				cnt++;
			}
			else{
				temp = i;
				diffVal = temp%10-(temp/10)%10;
				while(temp/10 != 0){
					if(diffVal != (temp%10-(temp/10)%10)){
						temp=99;
						break;
					}
					else{
						diffVal = temp%10-(temp/10)%10;
						temp = temp/10;
					}	
				}
				if(temp != 99){
					cnt++;
				}
			}
		}		
		in.close();
		System.out.println(cnt);
	}
	
	public static void print19() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int k = (int)Math.getExponent(N/3);
		String arr[]= new String[N];
		arr[0]="  *  ";
		arr[1]=" * * ";
		arr[2]="*****";
		for(int i=1; i<=k; i++){
			makeStar(i, arr);
		}
		for(int i=0; i<N; i++){
			System.out.println(arr[i]);
		}
	}

	public static void makeStar(int i, String arr[]){
		int lineNum = 3*(int)Math.pow(2, i);
		for(int l=lineNum/2; l<lineNum; l++){
			arr[l]=arr[l-lineNum/2]+" "+arr[l-lineNum/2];
		}
		for(int l=0; l<(lineNum/2); l++){
			for(int q=0; q<lineNum/2; q++){
				arr[l]=" "+arr[l]+" ";
			}
		}
	}
	
	public static void calWord() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String str = in.readLine();
		int cnt = 0;
		int flag = 0;
		if(str.length()==0)
			System.out.println(cnt);
		else{
			for(int i=0; i<str.length(); i++){
				if(str.charAt(i)!=' ' && flag == 0){
					flag=1;
					cnt++;
				}
				else if(str.charAt(i)==' ' && flag == 1){
					flag=0;
				}
			}
			System.out.println(cnt);
		}
	}
	
	public static void calRadix() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int A = Integer.parseInt(in .readLine());
		int B = Integer.parseInt(in .readLine());
		int C = Integer.parseInt(in .readLine());
		
		int result = A*B*C;
		int arr[]= new int[10];
		
		while(result/10 != 0){
			arr[result%10]++;
			result= result/10;
		}
		arr[result%10]++; //마지막 한번 더
		
		for(int i=0; i<10; i++){
			System.out.println(arr[i]);
		}
	}

	public static void calPoint() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		String[] str = new String[T];
		int[] arr = new int[T];
		for(int i=0; i<T; i++){
			str[i]=in.readLine();
			arr[i]=calPointA(str[i]);
			System.out.println(arr[i]);
		}
	}
	
	public static int calPointA(String str){
		int cnt=0;
		int sum=0;
		for(int i=0; i<str.length(); i++){
			if(str.charAt(i)=='O'){
				cnt++;
				sum=sum+cnt;
			}
			else
				cnt=0;
		}
		return sum;
	}
	
	public static void print20() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		int cnt = st.countTokens();
		int arr[] = new int[cnt];
		
		for(int i=0; i<cnt; i++){
			arr[i]=Integer.parseInt(st.nextToken());
		}
		int flag = 0;
		for(int i=0; i<arr.length-1; i++){
			if(Math.abs(arr[i]-arr[i+1])!=1){
				flag = 1;
			}		
		}
		if(flag == 1)
			System.out.println("mixed");
		else if(flag == 0 && arr[0] == 1)
			System.out.println("ascending");
		else
			System.out.println("descending");
		
	}
	
	public static void calAvg3() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int arr[] = new int[5];
		int sum = 0;
		int avg = 0;
		for(int i=0; i<5; i++){
			arr[i]=Integer.parseInt(in.readLine());
			if(arr[i]<40)
				arr[i]=40;
		}
		for(int i=0; i<5; i++){
			sum = sum+arr[i];
		}
		avg = sum/5;
		System.out.println(avg);
	}
	
	public static void printAscii() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String str = in.readLine();
		char ch = str.charAt(0);
		System.out.println((int)ch);
	}
	
	public static void printAlpha() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String str = in.readLine();
		int arr[] = new int[26];
		
		for(int i=0; i<26; i++){
			arr[i]=-1;
		}
		
		for(int i=0; i<str.length();i++){
			if(arr[str.charAt(i)-97] == -1)
				arr[str.charAt(i)-97]=i;
		}
		
		for(int i=0; i<26; i++){
			System.out.print(arr[i]);
			if(i == 25)
				break;
			System.out.print(" ");
		}
	}
	
	public static void printReChar() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		for(int i=0; i<T; i++){
			StringTokenizer st = new StringTokenizer(in.readLine());
			String temp = "";
			int N = Integer.parseInt(st.nextToken());
			String str = st.nextToken();
			for(int j=0; j<str.length(); j++){
				for(int k=0; k<N; k++){
					temp= temp+str.charAt(j);
				}
			}
			System.out.println(temp);
		}
	}
	
	public static void countChar() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String str = in.readLine();
		str=str.toUpperCase();
		int cnt[] = new int[26];
		int max = 0;
		int maxIndex = 99;
		int maxCnt = 0;
		for(int i=0; i<str.length(); i++){
			cnt[str.charAt(i)-65]++;
			if(cnt[str.charAt(i)-65]>max){
				max=cnt[str.charAt(i)-65];
				maxIndex=str.charAt(i)-65;
			}
		}
		for(int i=0; i<26; i++){
			if(cnt[i]==max)
				maxCnt++;
		}
		if(maxCnt > 1)
			System.out.println("?");
		else
			System.out.println((char)(maxIndex+65));
	}
	
	public static void calBigger() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int[] temp = new int[3];
		int[] temp2 = new int[3];
		for(int i=0; i<3; i++){
			temp[i]=A%10;
			A=A/10;
			temp2[i] = B%10;
			B=B/10;
		}
		A=temp[0]*100+temp[1]*10+temp[2];
		B=temp2[0]*100+temp2[1]*10+temp2[2];
		if(A>B)
			System.out.println(A);
		else
			System.out.println(B);
	}
	
	public static void groupWord() throws IOException{

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		int cnt = 0;
		
		for(int i=0; i<T; i++){
			
			String str = in.readLine();
			int arr[] = new int[26];
			int strLen = str.length();
			int j = 0;
			for(j=0; j<strLen; j++){
				if(arr[str.charAt(j)-97]==0)
					arr[str.charAt(j)-97]=1;
				else{
					if(str.charAt(j)==str.charAt(j-1))
						continue;
					else
						break;
				}	
			}
			if(j==strLen)
				cnt++;
		}
		System.out.println(cnt);
	}
	
	public static void dialTime() throws IOException{
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String str = in.readLine();
		int strLen = str.length();
		int arr[] = new int[10];
		int sum = 0;
		
		for(int i=0; i<strLen; i++){
			if('A'<=str.charAt(i) && str.charAt(i)<='C')
				arr[2]++;
			else if('D'<=str.charAt(i) && str.charAt(i)<='F')
				arr[3]++;
			else if('G'<=str.charAt(i) && str.charAt(i)<='I')
				arr[4]++;
			else if('J'<=str.charAt(i) && str.charAt(i)<='L')
				arr[5]++;
			else if('M'<=str.charAt(i) && str.charAt(i)<='O')
				arr[6]++;
			else if('P'<=str.charAt(i) && str.charAt(i)<='S')
				arr[7]++;
			else if('T'<=str.charAt(i) && str.charAt(i)<='V')
				arr[8]++;
			else if('W'<=str.charAt(i) && str.charAt(i)<='Z')
				arr[9]++;
			else
				continue;
		}
		
		for(int i=2; i<10; i++){
			sum = sum+arr[i]*(i+1);
		}
		
		System.out.println(sum);
	}
	
	public static void calChroAlpa() throws IOException{
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String str = in.readLine();
		int strLen = str.length();
		int cnt = 0;
		
		for(int i=0; i<strLen-1; i++){
			if(str.charAt(i)=='c'){
				if(str.charAt(i+1)=='-' || str.charAt(i+1)=='='){
					cnt++;
					i+=1;
				}
				else
					cnt++;
			}
			else if(str.charAt(i)=='d'){
				if(str.charAt(i+1)=='z' && str.charAt(i+2)=='='){
					cnt++;
					i+=2;
				}
				else if(str.charAt(i+1)=='-'){
					cnt++;
					i+=1;
				}
				else
					cnt++;
			}
			else if(str.charAt(i)=='l' || str.charAt(i)=='n'){
				if(str.charAt(i+1)=='j'){
					cnt++;
					i+=1;
				}
				else
					cnt++;
			}
			else if(str.charAt(i)=='s' || str.charAt(i)=='z'){
				if(str.charAt(i+1)=='='){
					cnt++;
					i+=1;
				}
				else
					cnt++;
			}
			else
				cnt++;
		}
		
		if(str.charAt(strLen-2)=='c'){
			if(str.charAt(strLen-1)=='-' || str.charAt(strLen-1)=='='){
			}
			else
				cnt++;
		}
		else if(str.charAt(strLen-3)=='d'){
			if(str.charAt(strLen-2)=='z' && str.charAt(strLen-1)=='='){
			}
			else 
				cnt++;
		}
		else if(str.charAt(strLen-2)=='d'){
			if(str.charAt(strLen-1)=='-'){
			}
			else
				cnt++;
		}
		else if(str.charAt(strLen-2)=='l' || str.charAt(strLen-2)=='n'){
			if(str.charAt(strLen-1)=='j'){
			}
			else
				cnt++;
		}
		else if(str.charAt(strLen-2)=='s' || str.charAt(strLen-2)=='z'){
			if(str.charAt(strLen-1)=='='){
			}
			else
				cnt++;
		}
		else
			cnt++;
		
		System.out.println(cnt);
	}
	
	public static void minDistance() throws IOException{
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int i = 1;
		int sum=1;
		
		while(sum<N){
			i=i+1;
			sum=sum+6*(i-1);
		}
		System.out.println(i);
	}
	
	public static void calDistance() throws IOException{
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int sum = 0;
		int i = 0; //줄 인덱스
		while(sum<N){
			i++;
			sum=sum+i;
		}
		if( i%2 == 0){
			System.out.println((i-(sum-N))+"/"+(1+(sum-N)));
		}
		else{
			System.out.println((1+(sum-N))+"/"+(i-(sum-N)));
		}
	}
	
	public static void calDistance2() throws IOException{
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		for(int i=0; i<T; i++){
			StringTokenizer st = new StringTokenizer(in.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int dist = y-x;
			int cnt = 0;//이동회수
			int moveDist = 0;//이동거리
			
			while(dist != 0){
					if(dist-(moveDist+1)*2>=0){//
						moveDist++;
						dist=dist-moveDist*2;
						cnt=cnt+2;
						//System.out.println("moveDist : "+moveDist+"*2"+" cnt : "+cnt);
					}
					else	if(dist-(moveDist+1)==0){//
						moveDist++;
						dist=dist-moveDist;
						cnt++;
						//System.out.println("moveDist : "+moveDist+" cnt : "+cnt);
					}
					else if(dist-(moveDist)>=0){
						dist=dist-moveDist;
						cnt++;
						//System.out.println("moveDist : "+moveDist+" cnt : "+cnt);
					}
					else if(dist-(moveDist-1)>=0){
						moveDist--;
						dist=dist-moveDist;
						cnt++;
						//System.out.println("moveDist : "+moveDist+" cnt : "+cnt);
					}
					else{
						moveDist--;
					}
			}
			
			System.out.println(cnt);
		}
		
	}
	
	 public static void CalRoomNum() throws IOException{
	        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	        int T = Integer.parseInt(in.readLine());
	        for(int t=0; t<T; t++){
	            StringTokenizer st = new StringTokenizer(in.readLine());
	            int H = Integer.parseInt(st.nextToken()); 
	            int W = Integer.parseInt(st.nextToken()); 
	            int N = Integer.parseInt(st.nextToken()); 
	            for(int i=0; i<W; i++){
	                for(int j=0; j<H; j++){
	                    N--;
	                    if(N==0){
	                        int sum=(j+1)*100+(i+1);
	                        System.out.println(sum);
	                        break;
	                    }
	                }
	                if(N==0){
	                    break;
	                }
	            }
	        }
	 }
	 
	 public static void CalApartCount() throws IOException{
	        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	        int T = Integer.parseInt(in.readLine());
	        for(int i=0; i<T; i++){
	            int K = Integer.parseInt(in.readLine());
	            int N = Integer.parseInt(in.readLine());
	            int arr[][] = new int[15][15];
	            for(int j=1; j<=N; j++){
	                arr[0][j]=j;
	            }
	            for(int p=1; p<=K; p++){
	                for(int q=1; q<=N; q++){
	                    int sum=0;
	                    for(int r=1; r<=q; r++){
	                       sum=sum+arr[p-1][r];
	                    }
	                    arr[p][q]=sum;
	                }
	            }
	            System.out.println(arr[K][N]);
	        }
	 }
	 
	 
	 public static void CalNeedSet() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int arr[] = new int[10];
		 int max = 0;
		 while(N/10 != 0){
			 arr[N%10]++;
			 N=N/10;
		 }
		 arr[N%10]++;
		 arr[6]=(arr[6]+arr[9]+1)/2;
		 for(int i=0; i<9; i++){
			if(arr[i]>max)
				max=arr[i];
		 }
		 System.out.println(max);
	 }
	 
	 public static void CalSetOrder() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int T = Integer.parseInt(in.readLine());
		 for(int i=0; i<T; i++){
			 StringTokenizer st= new StringTokenizer(in.readLine());
			 int M = Integer.parseInt(st.nextToken());
			 int N = Integer.parseInt(st.nextToken());
			 int X = Integer.parseInt(st.nextToken());
			 int Y = Integer.parseInt(st.nextToken());
			 
			 int x = 1;
			 int y = 1;
			 int cnt = 1;
			 int lcd=CalLcd(M,N);
			 
			 if(X==x && Y==y){
				 System.out.println(cnt);
				 return;
			 }
			 
			 while(cnt <= lcd){
				 int a=0;
				 int b=0;
				
				 if(X-x<0)
					 a=M+X-x;
				 else if(X-x==0)
					if(M==1)
						a=1;
					else
					    a=M;
				 else
					 a=X-x;
			
				 if(Y-y<0)
					 b=N+Y-y;
				 else if(Y-y==0)
					 if(N==1)
						 b=1;
					 else
						 b=N;
				 else
					 b=Y-y;
				
				 if(a>b){
					 x=(x+b)%M;
					 cnt=cnt+b;
					 y=(y+b)%N;
					 if(x==0)
						 x=M;
					 if(y==0)
						 y=N;
				 //System.out.println("a=>"+a+" b=>"+b+" x=>"+x+"y=>"+y+"cnt"+cnt);
					 if(X==x && Y==y){
						 System.out.println(cnt);
						 break;
					 }
				 }
				 else if(a<b){
					 y=(y+a)%N;
					 cnt=cnt+a;
					 x=(x+a)%M;
					 if(x==0)
						 x=M;
					 if(y==0)
						 y=N;
					//System.out.println("a=>"+a+" b=>"+b+" x=>"+x+"y=>"+y+"cnt"+cnt);
					 if(X==x && Y==y){
						 System.out.println(cnt);
						 break;
					 }
				 }
				 else{
					 y=y+a;
					 cnt=cnt+a;
					 x=X;
					//System.out.println("a=>"+a+" b=>"+b+" x=>"+x+" y=>"+y+" cnt"+cnt);
					 if(X==x && Y==y){
						 System.out.println(cnt);
						 break; 
					 }
				 }
			 }
			 if(cnt>lcd)
				 System.out.println("-1");
			 
		 }
	 }
	 
	 public static int CalLcd(int a, int b) throws IOException{
		 int Lcd = a*b;
		 int Gcd = 0;
		 int temp = 0;
		 if(a<b){
			temp=a;
			a=b;
			b=temp;
		 }
		 while(a%b != 0){
			temp=b;
			b=a%b;
			a=temp;
		 }
		 Gcd = b;
		 Lcd = Lcd/Gcd;
		 
		 return Lcd;
	 }
	 
	 public static void NOrdering() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int arr[] = new int[N];
		 int temp = 0;
		 for(int i=0; i<N; i++){
			 arr[i]=Integer.parseInt(in.readLine());
		 }
		 for(int i=0; i<N; i++){
			 for(int j=i; j<N; j++){
				 if(arr[i]>arr[j]){
					 temp=arr[i];
					 arr[i]=arr[j];
					 arr[j]=temp;
				 }
			 }
		 }
		 for(int i=0; i<N; i++){
			 System.out.println(arr[i]);
		 }
	 }
	 
	 public static void NOrdering2() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int arr[] = new int[N];
		 for(int i=0; i<N; i++){
			 arr[i]=Integer.parseInt(in.readLine());
		 }
		 MergeSort(arr);
		 for(int i=0; i<N; i++){
			 System.out.println(arr[i]);
		 }
	 }
	 
	 public static void MergeSort(int[] arr) {
		 MergeDivide(arr);
	 }
	 
	 public static void MergeDivide(int[] arr){
		 
		 if(arr.length == 1)
			 return;
		 
		 int divide1[]=new int[arr.length/2];
		 int divide2[]=new int[arr.length-arr.length/2];
		 
		 for(int i=0; i<arr.length/2; i++){
			 divide1[i]=arr[i];
			// System.out.println("divide1 => "+divide1[i]);
		 }
		 for(int i=0; i<arr.length-arr.length/2; i++){
			 divide2[i]=arr[i+arr.length/2];
			// System.out.println("divide2 => "+divide2[i]);
		 }
		 MergeDivide(divide1);
		 MergeDivide(divide2);
		 Merge(arr,divide1,divide2);
	/*	 for(int i=0; i<arr.length; i++){
			 System.out.print(i+" => "+arr[i]+" ");
		 }
		 System.out.println();
	*/
	 }
	 
	 public static void Merge(int[] arr, int[] divide1, int[] divide2){
		 int arrLen = arr.length;
		 int divide1Len = divide1.length;
		 int divide2Len = divide2.length;
		 int arrIndex = 0;
		 int divide1Index = 0;
		 int divide2Index = 0;
		 
		 while(arrIndex != arrLen){
			 if(divide1Index != divide1Len && divide2Index != divide2Len){
				 if(divide1[divide1Index]<divide2[divide2Index]){
					 arr[arrIndex]=divide1[divide1Index];
					 arrIndex++;
					 divide1Index++;
				 }
				 else{
					 arr[arrIndex]=divide2[divide2Index];
					 arrIndex++;
					 divide2Index++;
				 }
			 }
			 else{
				 if(divide1Index != divide1Len){
					 arr[arrIndex]=divide1[divide1Index];
					 arrIndex++;
					 divide1Index++;
				 }
				 else{
					 arr[arrIndex]=divide2[divide2Index];
					 arrIndex++;
					 divide2Index++;
				 }
			 }
		 }
	 }
	 
	 public static void NOrdering3() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int arr[] = new int[10001];
		 
		 int input = 0;
		 int max = 0;
		 
		 for(int i=0; i<N; i++){
			 input =Integer.parseInt(in.readLine());
			 arr[input]++;
			 if(max<input)
				 max=input;
		 }
		 
		 in.close();
		 OutputStream os = new BufferedOutputStream(System.out);
		 
		 for(int i=1; i<=max; i++){
			 if(arr[i]>0){
				 for(int j=0; j<arr[i]; j++){
					 os.write((i+"\n").getBytes());
				 }
			 }
		 }
		 os.flush(); 
		 os.close();
	 }
	 
	 public static void Statistics() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int arr[] = new int[N];
		 int indexArr[] = new int[8001];
		 double avg = 0;
		 int median = 0;
		 int freqNum = 0;
		 int range = 0;
		 int maxFreq = 0;
		 
		 for(int i=0; i<N; i++){
			 arr[i]=Integer.parseInt(in.readLine());
			 indexArr[4000+arr[i]]++; 
			 if(indexArr[4000+arr[i]]>maxFreq){
				 maxFreq=indexArr[4000+arr[i]];
			 }
			 avg = avg + arr[i];
		 }
		 
		 MergeSort(arr);
		 
		 int cnt=0;
		 int freqArr[] = new int[N];
		 for(int i=0; i<indexArr.length; i++){
			 if(indexArr[i]==maxFreq){
				 freqArr[cnt]=i-4000;
				 cnt++;
			 }
		 }
		 if(cnt==1){
			 freqNum = freqArr[0];
		 }
		 else{
			 freqNum = freqArr[1];
		 }
		 
		 avg = Math.round(avg/N);
		 median = arr[(arr.length)/2];
		 range = arr[arr.length-1]-arr[0];
		 
		 in.close();
		 
		 OutputStream os = new BufferedOutputStream(System.out);
		 os.write(((int)avg+"\n").getBytes());
		 os.write((median+"\n").getBytes());
		 os.write((freqNum+"\n").getBytes());
		 os.write((range+"\n").getBytes());
		 
		 os.flush();
		 os.close();
	 }
	 
	 
	 public static void RadixSorting() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int arr[] = new int[10];
		 int cnt = 0;
		 int temp = 0;
		 while(N/10 != 0){
			 arr[cnt++]=N%10;
			 N=N/10;
		 }
		 arr[cnt++]=N%10;
		 
		 for(int i=0; i<cnt; i++){
			 for(int j=i; j<cnt; j++){
				 if(arr[i]<arr[j]){
					 temp=arr[i];
					 arr[i]=arr[j];
					 arr[j]=temp;
				 }
			 }
		 }
		 
		 for(int i=0; i<cnt; i++){
			 System.out.print(arr[i]);
		 }
	 }
	 
	 
	 public static void WordSorting() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 String arr[] = new String[N];
		 String sortArr[] = new String[N];
		 String tempStr = "";
		 int cnt = 0;
		 
		 for(int i=0; i<N; i++){		 
			 arr[i]=in.readLine();
		 }
		 in.close();
		 
		 MergeSort2(arr);
		 
		 for(int i=0; i<N; i++){
			 if(tempStr.equals(arr[i])){
				 continue;
			 }
			 else{
				 tempStr = arr[i];
				 sortArr[cnt++] = arr[i];
			 }
		 }
		 
		 OutputStream os = new BufferedOutputStream(System.out);
		 for(int i=0; i<cnt; i++)	
			 os.write((sortArr[i]+"\n").getBytes());
		 os.flush();
		 os.close();
	 }
	 
	 public static void MergeSort2(String[] arr){
		 MergeDivide2(arr);
	 }
	 
	 public static void MergeDivide2(String[] arr){
		 
		 if(arr.length == 1)
			 return;
		 
		 String divide1[] = new String[arr.length/2];
		 String divide2[] = new String[arr.length-arr.length/2];
		 for(int i=0; i<arr.length/2; i++){
			 divide1[i]=arr[i];
		 }
		 for(int i=0; i<arr.length-arr.length/2; i++){
			 divide2[i]=arr[i+arr.length/2];
		 }
		 MergeDivide2(divide1);
		 MergeDivide2(divide2);
		 Merge2(arr, divide1, divide2);
	 }
	 
	 public static void Merge2(String[] arr, String[] divide1, String[] divide2){
		 int arrLen = arr.length;
		 int divide1Len = divide1.length;
		 int divide2Len = divide2.length;
		 int arrIndex = 0;
		 int divide1Index=0;
		 int divide2Index=0;
		 
		 while(arrLen != arrIndex){
			 if(divide1Len != divide1Index && divide2Len != divide2Index){
				 if(divide1[divide1Index].length()<divide2[divide2Index].length()){
					 arr[arrIndex++]=divide1[divide1Index++];
				 }
				 else if(divide1[divide1Index].length()>divide2[divide2Index].length()){
					 arr[arrIndex++]=divide2[divide2Index++];
				 }
				 else{
					 if(divide1[divide1Index].equals(divide2[divide2Index])){
						arr[arrIndex++]=divide1[divide1Index++]; 
					 }
					 else{
						 for(int i=0; i<divide1[divide1Index].length(); i++){
							 if(divide1[divide1Index].charAt(i)<divide2[divide2Index].charAt(i)){
								 arr[arrIndex++]=divide1[divide1Index++];
								 break;
							 }
							 else if(divide1[divide1Index].charAt(i)>divide2[divide2Index].charAt(i)){
								 arr[arrIndex++]=divide2[divide2Index++];
								 break;
							 }
							 else
								 continue;
						 }
					 }
				 }
			 }
			 else{
				 if(divide1Len != divide1Index){
					 arr[arrIndex++]=divide1[divide1Index++];
				 }
				 else{
					 arr[arrIndex++]=divide2[divide2Index++];
				 }
			 }
		 }
	 }
	 
	 public static void Decimal() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int arr[] = new int[N];
		 int count = 0;
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 int arrLen = st.countTokens();
		 for(int i=0; i<arrLen; i++){
			 arr[i] = Integer.parseInt(st.nextToken());
		 }
		 for(int i=0; i<arr.length; i++){
			 for(int j=1; j<=arr[i]; j++){
				 if(arr[i]%j==0 && j==1){
					 continue;
				 }
				 else if(arr[i]%j==0 && j==arr[i]){
					 count++;
				 }
				 else if(arr[i]%j==0){
					 break;
				 }
				 else{
					 continue;
				 }
			 }
		 }
		 System.out.println(count);
	 }
	 
	 public static void Decimal2() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int M = Integer.parseInt(in.readLine());
		 int N = Integer.parseInt(in.readLine());
		 int sum = 0;
		 int min = 10001;
		 int count = 0;
		 for(int i=M; i<=N; i++){
			 for(int j=1; j<=i; j++){
				 if(i%j==0 && j==1){
					 continue;
				 }
				 else if(i%j==0 && j==i){
					sum+=i;
					count++;
					if(min>i)
						min=i;
				 }
				 else if(i%j==0){
					 break;
				 }
				 else{
					 continue;
				 }
			 }
		 }
		 if(count == 0){
			 System.out.println("-1");
		 }
		 else{
			 System.out.println(sum);
			 System.out.println(min);
		 }
	 }
	 
	 public static void Decimal3() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 int M = Integer.parseInt(st.nextToken());
		 int N = Integer.parseInt(st.nextToken());
		 in.close();
		 
		 int arr[] = new int[N+1];
		 
		 for(int i=2; i<=N; i++){
			 if(arr[i]==0){
				 if(i<Math.sqrt(N)){
					 for(int j=i*i; j<=N; j+=i){
						 arr[j]=1;
					 }
				 }
			 }
		 }
		 for(int i=M; i<=N; i++){
			 if(arr[i]==0 && i>=2)
				 System.out.println(i);
		 }
	 }
	 
	 public static void Decimal4() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = 0;
		 int cnt = 0;
		 do{
			 cnt=0;
			 N = Integer.parseInt(in.readLine());
			 if(N==0)
				 break;
			 int arr[] = new int[N*2+1];
			 for(int i=2; i<=2*N; i++){
				 if(arr[i]==0){
					 if(i<=Math.sqrt(2*N)){
						 for(int j=i*i; j<=2*N; j+=i){
							 arr[j]=1;
						 }
					 }
				 }
			 }
			 for(int i=N+1; i<=2*N; i++){
				 if(arr[i]==0 && i>=2)
					 cnt++;
			 }
			 System.out.println(cnt);
		 }while(N!=0);
	 }
	 
	 public static void Decimal5() throws IOException{ //골드바흐 파티션
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int T = Integer.parseInt(in.readLine());
		 for(int t=0; t<T; t++){
			 int N = Integer.parseInt(in.readLine());
			 int arr[] = new int[N+1];
			 int destArr[] = new int[N+1];
			 int cnt = 0;
			 int goldBagh1 = 0;
			 int goldBagh2 = 0;
			 int diffBagh=10000;
			 
			 for(int i=2; i<=N; i++){
				 if(arr[i]==0){
					 if(i<Math.sqrt(N)){
						 for(int j=i*i; j<=N; j+=i){
							 arr[j]=1;
						 }
					 }
				 }
			 }
			 for(int i=2; i<=N; i++){
				 if(arr[i]==0 && i>=2){
					 destArr[cnt]=i;
					 cnt++;
				//	 System.out.println(i);
				 }
			 }
			 for(int i=0; i<cnt; i++){
				 for(int j=i; j<cnt; j++){
					 if(destArr[i]+destArr[j] == N && destArr[j]-destArr[i]<diffBagh){
						 goldBagh1=destArr[i];
						 goldBagh2=destArr[j];
						 diffBagh=destArr[j]-destArr[i];
				//		 System.out.println(goldBagh1);
				//		 System.out.println(goldBagh2);
				//		 System.out.println(diffBagh);
					 }
				 }
			 }
			 
			 System.out.println(goldBagh1+" "+goldBagh2);
		 }
		 
	 }
	 public static void Stack() throws IOException{
		 int arr[] = new int[10000];
		 int top = 0;
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int T = Integer.parseInt(in.readLine());
		 for(int i=0; i<T; i++){
			 StringTokenizer st = new StringTokenizer(in.readLine());
			 String inst = st.nextToken();
			 if(inst.equals("push")){
				 top=Push(arr,top,Integer.parseInt(st.nextToken()));
				 //System.out.println("Pushed top: "+top+", Pushed Value: "+arr[top]);
			 }
			 else if(inst.equals("pop")){
				 if(top==0){
					 System.out.println("-1");
				 }
				 else{
					 top=Pop(arr,top);
					 System.out.println(arr[(top+1)]);
					 //System.out.println("Poped top: "+(top+1)+", Poped Value: "+arr[(top+1)]);
				 }
			 }
			 else if(inst.equals("size")){
				 System.out.println(top);
			 }
			 else if(inst.equals("empty")){
				 if(top==0){
					 System.out.println("1");
				 }
				 else{
					 System.out.println("0");
				 }
			 }
			 else if(inst.equals("top")){
				 if(top==0){
					 System.out.println("-1");
				 }
				 else{
					 System.out.println(arr[(top)]);
					 //System.out.println("top Index: "+top+", top Value: "+arr[top]);
				 }
			 }
		 }
		 
	 }
	 
	 public static int Push(int[] arr, int top, int X){
		 arr[++top]=X;
		 return top;
	 }
	 
	 public static int Push(String[] arr, int top, String X){
		 arr[++top]=X;
		 return top;
	 }
	 
	 public static int Pop(int[] arr, int top){
		 if(top==0)
			 return top;
		 else
			 return --top;
	 }
	 
	 public static int Pop(String[] arr, int top){
		 if(top==0)
			 return top;
		 else
			 return --top;
	 }
	 
	 public static void Stack2() throws IOException{
		 int arr[] = new int[100000];
		 String strArr[] = new String[200000];
		 int top = 0;
		 int cnt = 0;
		 int cnt2 = 0;
		 int cnt3 = 0;
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int originArr[] = new int[N];
		 int destArr[] = new int[N];
		 for(int i=0; i<N; i++){
			 destArr[i]=Integer.parseInt(in.readLine());
		 }
		 for(int i=0; i<N; i++){
			 originArr[i]=i+1;
		 }
		 while(true){
			 if(top==0 && cnt2==N)
				 break;
			 else if(arr[top]!=destArr[cnt2]){
				 if(cnt==N){
					 break;
				 }
				 top=Push(arr,top,originArr[cnt]);
				 strArr[cnt3++]="+";
				 cnt++;
			 }
			 else{
				 top=Pop(arr,top);
				 strArr[cnt3++]="-";
				 cnt2++;
			 }
		 }
		 if(top>0){
			 System.out.println("NO");
		 }
		 else{
			for(int i=0; i<cnt3; i++){
				System.out.println(strArr[i]);
			}
		 }
	 }
	 
	 public static void Stack3() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int T = Integer.parseInt(in.readLine());
		 int arr[] = new int[51];
		 for(int i=0; i<T; i++){
			String str = in.readLine();
			int strLen = str.length();
			int top = 0;
			int j = 0;
			for(j=0; j<strLen; j++){
				if(str.charAt(j)=='('){
					top = Push(arr, top, 1);
				}
				else{
					if(top == 0)
						break;
					else
						top = Pop(arr, top);
				}
			}
			if(j == strLen && top == 0){
				System.out.println("YES");
			}
			else{
				System.out.println("NO");
			}
		 }
	 }
	 
	 public static void Stack4() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 String str = in.readLine();
		 int strLen = str.length();
		 int top = 0;
		 String arr[] = new String[strLen+1];
		 int arrLen = arr.length;
		 int i = 0;
		 int temp=0;
		 
		 for(int z=0; z<strLen+1; z++){
			 arr[z]="0";
		 }
		 
		 for(i=0; i <strLen; i++){
			 
			 if(str.charAt(i)=='('){
				 top = Push(arr,top,"(");
				 //Print99(arr);
			 }
			 else if(str.charAt(i)=='['){
				 top = Push(arr,top,"[");
				 //Print99(arr);
			 }
			 else if(str.charAt(i)==']'){
				 //Print99(arr);
				 if(top==0)
					 break;
				 if(arr[top]=="(" || Check1(arr,"[",arrLen)==-1)
					 break;
				 else{
					 if(arr[top]=="["){
						 arr[top]="0";
						 top = Pop(arr,top);
						 top = Push(arr,top,"3");
					 }				
					 else{
						 int z=0;
						 int index=Check1(arr,"[",arrLen);
						 for(z=top; z>index; z--){
							 temp = temp + Integer.parseInt(arr[z]);
							 arr[z]="0";
							 top = Pop(arr,top);
						 }
						 arr[top]="0";
						 top = Pop(arr,top);
						 top = Push(arr,top,String.valueOf(temp*3));
						 temp = 0;
					 }
				 }
				 //Print99(arr);
			 }
			 else if(str.charAt(i)==')'){
				 //Print99(arr);
				 if(top==0)
					 break;
				 if(arr[top]=="[" || Check1(arr,"(",arrLen)==-1)
					 break;
				 else{
					 if(arr[top]=="("){
						 arr[top]="0";
						 top = Pop(arr,top);
						 top = Push(arr,top,"2");
					 }				
					 else{
						 int z=0;
						 int index=Check1(arr,"(",arrLen);
						 for(z=top; z>index; z--){
							 temp = temp + Integer.parseInt(arr[z]);
							 arr[z]="0";
							 top = Pop(arr,top);
						 }
						 arr[top]="0";
						 top = Pop(arr,top);
						 top = Push(arr,top,String.valueOf(temp*2));
						 temp = 0;
					 }
				 }
				 //Print99(arr);
			 }
			 else
				 break;
		 }
		 if((top==0 && strLen == 1) || (i<strLen) || Check1(arr,"(",arrLen)>0||Check1(arr,"[",arrLen)>0||Check1(arr,"]",arrLen)>0||Check1(arr,")",arrLen)>0){
			 System.out.println("0");
		 }
		 else{
			 for(int t=0; t<arrLen; t++){
					 temp = temp + Integer.parseInt(arr[t]);
			 }
			 System.out.println(temp);
		 }	 
	 }
	 
	 public static int Check1(String[] arr, String str, int arrLen){
		 int flag=-1;
		 for(int j=0; j<arrLen; j++){
			 if(arr[j] != null){
				 if(arr[j].equals(str))
					 flag=j;
			 }
		 }
		 return flag;
	 }
	 
	 
	 public static void Queue() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = null;
		 int queue[] = new int[10000];
		 int front=0;
		 int back=0;
		 int T = Integer.parseInt(in.readLine());
		 for(int i=0; i<T; i++){
			 st = new StringTokenizer(in.readLine());
			 switch(st.nextToken()){
			 	case "push" :
			 		if(front==back && queue[back]==0){
			 			Push2(queue,back,Integer.parseInt(st.nextToken()));
			 			//Print99(queue);
			 		}
			 		else{
			 			Push2(queue,++back,Integer.parseInt(st.nextToken()));
			 			//Print99(queue);
			 		}
			 		break;
			 	case "pop" :
			 		if((front==back && queue[front]==0) )
			 			System.out.println("-1");
			 		else if(front==back && queue[front]!=0){
			 			System.out.println(queue[front]);
			 			Pop2(queue,front);
			 			front=0;
			 			back=0;
			 			//Print99(queue);
			 		}
			 		else{
			 			System.out.println(queue[front]);
			 			Pop2(queue,front++);
			 			//Print99(queue);
			 		}
			 		break;
			 	case "front" :
			 		if(queue[front]==0)
			 			System.out.println("-1");
			 		else
			 			System.out.println(queue[front]);
			 		break;
			 	case "back" :
			 		if(queue[back]==0)
			 			System.out.println("-1");
			 		else
			 			System.out.println(queue[back]);
			 		break;
			 	case "empty" :
			 		if(front==back && queue[front]==0)
			 			System.out.println("1");
			 		else
			 			System.out.println("0");
			 		break;
			 	case "size" :
			 		if(queue[front]==0 || queue[back]==0)
			 			System.out.println("0");
			 		else
			 			System.out.println(back-front+1);
			 		break;
			 }			 
		 }
		 in.close();
	 }
	 
	 public static void Push2(int[] arr, int back, int X){
		 arr[back]=X;
	 }
	 
	 public static void Pop2(int[] arr, int front){
		 arr[front]=0;
	 }
	 
	 public static void Print99(String[] arr){
		 for(int j=0; j<arr.length; j++){
			 System.out.print(arr[j]+" ");
		 }
		 System.out.println();
	 }
	 public static void Print99(int[] arr){
		 for(int j=0; j<arr.length; j++){
			 System.out.print(arr[j]+" ");
		 }
		 System.out.println();
	 }
	 
	 public static void Queue2() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 
		 int vertex = Integer.parseInt(st.nextToken());
		 int edge = Integer.parseInt(st.nextToken());
		 int initVertex = Integer.parseInt(st.nextToken());
		 int xIndex = 0;
		 int yIndex = 0;
		 int edgeArr[][] = new int[vertex+1][vertex+1]; //양방향간선.
		 int vertexArr[] = new int[vertex+1];
		 
		 int queue[] = new int[vertex+1];
		 int front = 1;
		 int back = 1;
		 
		 for(int i=0; i<edge; i++){ //인접행렬에 간선 입력
			 st = new StringTokenizer(in.readLine());
			 xIndex = Integer.parseInt(st.nextToken());
			 yIndex = Integer.parseInt(st.nextToken());
			 
			 edgeArr[xIndex][yIndex]=1;
			 edgeArr[yIndex][xIndex]=1;
		 }
		 
		 vertexArr[initVertex]=1;
		 Push2(queue,back,initVertex);
		 
		 back=DFS(edgeArr, vertexArr, initVertex, queue, back);
		 
		 for(int j=1; j<=back; j++){
			 System.out.print(queue[front]);
			 System.out.print(" ");
			 Pop2(queue,front++);
		 }
		 
		 System.out.println();
		 
		 for(int j=1; j<=vertex; j++){
			 vertexArr[j]=0; //방문정점 초기화
		 }
		 
		 
		 
		 front=1;
		 back=1;
		 vertexArr[initVertex]=1;
		 Push2(queue,back,initVertex);
		 
		 back=BFS(edgeArr, vertexArr, initVertex, queue, front, back);
		 
		 for(int j=1; j<=back; j++){
			 System.out.print(queue[front]);
			 System.out.print(" ");
			 Pop2(queue,front++);
		 }
		 
	 }
	 
	 public static int DFS(int[][] edgeArr, int[] vertexArr, int curVertex, int[] queue, int back){
		 for(int i=1; i<edgeArr[0].length; i++){
			 if(edgeArr[curVertex][i] == 1 && vertexArr[i] != 1){
				 vertexArr[i]=1;
				 Push2(queue,++back,i);
				 back = DFS(edgeArr,vertexArr,i,queue,back);
			//	 System.out.println("DFS: "+i);
			 }
		 }
		 return back;
	 }
	 
	 public static int BFS(int[][] edgeArr, int[] vertexArr, int curVertex, int[] queue,int front, int back){
		 do{
			 for(int i=1; i<edgeArr[0].length; i++){
				 if(edgeArr[curVertex][i] == 1 && vertexArr[i] != 1){
					 vertexArr[i]=1;
					 Push2(queue,++back,i);
				//	 System.out.println("BFS: "+i);
				 }
			 }
			 if(front == back) //연결된 간선이 없다면 종료
				 return back;
			 else{
				 front++;
				 curVertex=queue[front]; //큐의 다음 값을 인덱스로 저장
			 }
		 }while(queue[front]!=0); //인덱스가 0이라면 큐에 푸쉬된 연결 정점이 없기 때문에 종료.
		return back;
	 }
	 
	 public static void Queue3() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = null;
		 
		 int T = Integer.parseInt(in.readLine());
		 for(int i=0; i<T; i++){
			 st = new StringTokenizer(in.readLine());
			 int N = Integer.parseInt(st.nextToken());
			 int M = Integer.parseInt(st.nextToken());
			 int queue[] = new int[N+1];
			 int indexQueue[] = new int[N+1];
			 int resultQueue[] = new int[N+1];
			 int resultIndexQueue[] = new int[N+1];

			 int k=0;
			 int cnt=0;
			 
			 st = new StringTokenizer(in.readLine());
			 for(int j=0; j<N; j++){
				 queue[j] = Integer.parseInt(st.nextToken());
				 indexQueue[j] = j;
			 }
			 
			 while(N>=1){
				 for(k=1; k<N; k++){
					 if(queue[0]<queue[k]){  //큰게 있을경우 맨 앞의 값을 큐맨뒤로
						 queue[N]=queue[0];
						 indexQueue[N]=indexQueue[0];
						 for(int l=1; l<=N; l++){
							 queue[l-1]=queue[l];
							 indexQueue[l-1]=indexQueue[l];
						 }
						 queue[N]=0;
						 indexQueue[N]=0;
						 break;
					 }
				 }
				 if(k==N){ //없을 경우 큐에서 내보내고 큐의 크기 -1
					 resultQueue[cnt]=queue[0];
					 resultIndexQueue[cnt]=indexQueue[0];
					 cnt++;
					 for(int l=1; l<=N; l++){
						 queue[l-1]=queue[l];
						 indexQueue[l-1]=indexQueue[l];
					 }
					 queue[N]=0;
					 indexQueue[N]=0;
					 N=N-1;
				 }
			 }
			 for(int j=0; j<queue.length-1; j++){
				 if(resultIndexQueue[j]==M){
					 System.out.println(j+1);
					 break;
				 }
			 }
		 }
	 }
	 
	 public static void Queue4() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 
		 int N = Integer.parseInt(st.nextToken());
		 int M = Integer.parseInt(st.nextToken());
		 int cnt = 0;
		 int cnt2 = 0;
		 int temp = 0;
		 
		 int copyN = N;
		 
		 int queue[] = new int[N];
		 int resultArr[] = new int[N];
		 
		 for(int i=0; i<N; i++){
			 queue[i]=i+1;
		 }
		 
		 while(cnt2!=N){
			 cnt++;
			 if(cnt%M == 0){//Pop
				 temp = queue[0];
				 for(int j=1; j<copyN; j++){
					 queue[j-1]=queue[j];
				 }
				 copyN--;
				 resultArr[cnt2++]=temp;
			 }
			 else{//Pop,Push
				 temp = queue[0];
				 for(int j=1; j<copyN; j++){
					 queue[j-1]=queue[j];
				 }
				 queue[copyN-1]=temp;
			 }
		 }
		 
		 System.out.print("<");
		 for(int i=0; i<cnt2; i++){
			 if(i==cnt2-1)
				 System.out.print(resultArr[i]);
			 else
				 System.out.print(resultArr[i]+", ");
		 }
		 System.out.print(">");
	 }
	 
	 public static void Queue5() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 
		 int N = Integer.parseInt(st.nextToken());
		 int M = Integer.parseInt(st.nextToken());
		 int cnt = 0;
		 int cnt2 = 0;
		 
		 int queue[] = new int[N*N];
		 int resultArr[] = new int[N];
		 
		 for(int i=0; i<N; i++){
			 queue[i]=i+1;
		 }
		 
		 while(cnt2!=N){
			 cnt++;
			 if(cnt%M == 0){//Pop				 
				 resultArr[cnt2]=queue[cnt-1];
				 //System.out.println("pop index : "+(cnt-1));
				 cnt2++;	 
			 }
			 else{//Pop,Push
				 queue[N+(cnt-cnt2)-1]=queue[cnt-1];
				// System.out.println("push index : "+(N+(cnt-cnt2)-1));
			 }
		 }
		 
		 System.out.print("<");
		 for(int i=0; i<cnt2; i++){
			 if(i==cnt2-1)
				 System.out.print(resultArr[i]);
			 else
				 System.out.print(resultArr[i]+", ");
		 }
		 System.out.print(">");
	 }
	 
	 /*
	 public static void PriotyQueue() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = null;
		 
		 int T = Integer.parseInt(in.readLine());
		 for(int i=0; i<T; i++){
			 st = new StringTokenizer(in.readLine());
			 int N = Integer.parseInt(st.nextToken());
			 int M = Integer.parseInt(st.nextToken());
			 int value = 0;
			 int heapArr[] = new int[N+1];
			 int result = 0;
			 int resultArr[] = new int[N+1];
			 boolean heapVisit[] = new boolean[N+1];  // 중요도의 범위가 int 형이므로 0 또는 음수도 가능. 
			 heapArr[0] = 2147483647;
			 
			 st = new StringTokenizer(in.readLine());
			 for(int j=0; j<N; j++){
				 value = Integer.parseInt(st.nextToken());
				 resultArr[j+1]=value; //우선순위 큐에서 나오는 최대값들을 비교할 배열.
				 addHeap(heapArr,heapVisit,value);
			 }
			 for(int k=1; k<=N; k++){
				 result = removeHeap(heapArr,heapVisit);
				 if(result == resultArr[M+1]){
					 System.out.println(k);
					 break;
				 }
			 }
			 
		 }
		 in.close();
	 }
	 
	 public static void addHeap(int[] heapArr, boolean[] heapVisit, int value){
		 int cnt = 1; //heapArr[0]은 root 노드. 빈 값
		 int temp = 0;	
		 
		 while(heapVisit[cnt]!=false){//방문하지 않은 마지막 노드 인덱스 검색
			 cnt++;
		 }
		 heapArr[cnt] = value;
		 heapVisit[cnt] = true;
		 	 
		 while(heapArr[cnt] >= heapArr[cnt/2]){
			 temp = heapArr[cnt];
			 heapArr[cnt] = heapArr[cnt/2];
			 heapArr[cnt/2] = temp;
			 cnt = cnt/2;
		 }
	 }
	 
	 public static int removeHeap(int[] heapArr, boolean[] heapVisit){
		 int cnt=1;
		 int cnt2=1;
		 int maxValue = heapArr[1];
		 int temp = 0; 

		 while(heapVisit[cnt]!=false){//방문하지 않은 마지막 노드 인덱스 검색
			 cnt++;
			 if(cnt>=heapArr.length){
				 break;
			 }
		 }
		 cnt = cnt-1;
		 heapArr[1] = heapArr[cnt];
		 heapArr[cnt] = 0;
		 heapVisit[cnt] = false;
		 
		 if(cnt2*2 > cnt){
			 return maxValue;
		 }
		 while(heapArr[cnt2]<heapArr[cnt2*2] || heapArr[cnt2]<heapArr[cnt2*2+1]){
			 if(heapArr[cnt2*2]>heapArr[cnt2*2+1]){
				 temp = heapArr[cnt2*2];
				 heapArr[cnt2*2] = heapArr[cnt2];
				 heapArr[cnt2] = temp;
				 cnt2 = cnt2*2;
			 }
			 else{
				 temp = heapArr[cnt2*2+1];
				 heapArr[cnt2*2+1] = heapArr[cnt2];
				 heapArr[cnt2] = temp;
				 cnt2 = cnt2*2+1;
			 }
			 if(cnt2*2 >= cnt){
				 break;
			 }
		 }
		 
		 return maxValue;
	 }
	 */
	 
	 public static void Deck() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int deck[] = new int[100001];
		 int index[] = new int[2];
		 
		 for(int t=0; t<N; t++){	 
			 StringTokenizer st = new StringTokenizer(in.readLine());
			 switch(st.nextToken()){
			 	case "push_front" :
			 			Push_Front(deck,index,Integer.parseInt(st.nextToken()));
			 			break;
			 	case "push_back" : 
			 			Push_Back(deck,index,Integer.parseInt(st.nextToken()));
			 			break;
			 	case "pop_front" : 
			 			Pop_Front(deck,index);
			 			break;
			 	case "pop_back" : 
			 			Pop_Back(deck,index);
			 			break;
			 	case "size" :
			 			Deck_Size(deck,index);
			 			break;
			 	case "empty" : 
			 			Deck_Empty(deck,index);
			 			break;
			 	case "front" :
			 			Deck_Front_Value(deck,index);
			 			break;
			 	case "back" : 
			 			Deck_Back_Value(deck,index);
			 			break;
			 }
		 }
	 }
	 
	 public static  void Push_Front(int[] deck, int[] index, int X){ // index[0] : front, index[1] : back
		 if(index[0]==index[1]){
			 if(deck[index[0]]!=0){
				 deck[index[0]+1]=deck[index[0]];
				 deck[index[0]]=X;
				 index[1]++;
			 }
			 else{
				 deck[index[0]]=X;
			 }
		 }
		 else{
			 for(int i=index[1]; i>=index[0]; i--){
				 deck[i+1]=deck[i];
			 }
			 deck[index[0]]=X;
			 index[1]++;
		 }
	 }
	 
	 public static void Push_Back(int[] deck, int[] index, int X){
		 if(index[0]==index[1]){
		 	if(deck[index[0]]!=0){ 
		 		deck[index[1]+1]=X;
				 index[1]++;
		 	}
		 	else{
		 		deck[index[1]]=X;
		 	}
		 }
		 else{
			 deck[index[1]+1]=X;
			 index[1]++;
		 }
	 }
	 
	 public static void Pop_Front(int[] deck, int[] index){
		 if(index[0]==index[1]){
			 if(deck[index[0]]!=0){
				 //System.out.println(deck[index[0]]);
				 deck[index[0]]=0; 
			 }
			 else{
				 //System.out.println("-1");
			 }
		 }
		 else{
			 //System.out.println(deck[index[0]]);
			 deck[index[0]]=0;
			 index[0]++;
		 }
	 }
	 
	 public static void Pop_Back(int[] deck, int[] index){
		 if(index[0]==index[1]){
			 if(deck[index[1]]!=0){
				 //System.out.println(deck[index[1]]);
				 deck[index[1]]=0;
			 }
			 else{
				 //System.out.println("-1");
			 }
		 }
		 else{
			 //System.out.println(deck[index[1]]);
			 deck[index[1]]=0;
			 index[1]--;
		 }
	 }
	 
	 public static int Deck_Size(int[] deck, int[] index){
		 if(index[1]-index[0] == 0 && deck[index[1]]==0){
			 //System.out.println("0");
			 return 0;
		 }
		 else{
			 //System.out.println(index[1]-index[0]+1);
			 return index[1]-index[0]+1;
		 }
	 }
	 
	 public static void Deck_Empty(int[] deck, int[] index){
		 if(index[1]-index[0] == 0 && deck[index[1]]==0){
			 System.out.println("1");
		 }
		 else{
			 System.out.println("0");
		 }
	 }
	 
	 public static void Deck_Front_Value(int[] deck, int[] index){
		 if(index[0]==index[1] && deck[index[0]]==0){
			 System.out.println("-1");
		 }
		 else{
			 System.out.println(deck[index[0]]);
		 }
	 }
	 
	 public static void Deck_Back_Value(int[] deck, int[] index){
		 if(index[0]==index[1] && deck[index[1]]==0){
			 System.out.println("-1");
		 }
		 else{
			 System.out.println(deck[index[1]]);
		 }
	 }
	
	 public static void Deck2() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 int N = Integer.parseInt(st.nextToken());
		 int M = Integer.parseInt(st.nextToken());
		 int deck[] = new int[N*N]; //덱의 재정렬이 없기 때문에 모두 팝하고 푸쉬할 경우 최대 N*N/2의 인덱스까지 가질수 있음.
		 int index[] = new int[2];
		 int cnt = 0;
		 int cntSum = 0;
		 int deckSize = 0;
		 
		 for(int i=0; i<N; i++){
			 Push_Back(deck,index,i+1);
		 }
		 
		 st = new StringTokenizer(in.readLine());
		 for(int i=0; i<M; i++){
			 int destIndex = Integer.parseInt(st.nextToken());
			 if(destIndex==deck[index[0]]){
				 //System.out.println("before real Pop======front : "+index[0]+"back : "+index[1]);
				 //Print98(deck);
				 Pop_Front(deck,index);
				 //System.out.println("after real Pop======front : "+index[0]+"back : "+index[1]);
				 //Print98(deck);
			 }
			 else{
				 cnt = index[0];
				 while(destIndex!=deck[cnt]){
					 cnt++;
				 }
				 cnt = cnt-index[0];
				 deckSize = Deck_Size(deck,index);
				 if(cnt>deckSize/2){
					 for(int j=0; j<deckSize-cnt; j++){
						 //System.out.println("before=================================================front : "+index[0]+"back : "+index[1]);
						 //Print98(deck);
						 Push_Front(deck,index,deck[index[1]]);
						 //System.out.println("push======front : "+index[0]+"back : "+index[1]);
						 //Print98(deck);
						 Pop_Back(deck,index);
						 //System.out.println("pop======front : "+index[0]+"back : "+index[1]);
						 //Print98(deck);
					 }
					 cntSum=cntSum+deckSize-cnt;
				 }
				 else{
					 for(int j=0; j<cnt; j++){
						 //System.out.println("before======front : "+index[0]+"back : "+index[1]);
						 //Print98(deck);
						 Push_Back(deck,index,deck[index[0]]);
						 //System.out.println("push======front : "+index[0]+"back : "+index[1]);
						 //Print98(deck);
						 Pop_Front(deck,index);
						 //System.out.println("pop======front : "+index[0]+"back : "+index[1]);
						 //Print98(deck);
					 }
					 cntSum=cntSum+cnt;
				 }
				 if(destIndex==deck[index[0]]){
					 //System.out.println("before real Pop======front : "+index[0]+"back : "+index[1]);
					 //Print98(deck);
					 Pop_Front(deck,index);
					 //System.out.println("after real Pop======front : "+index[0]+"back : "+index[1]);
					 //Print98(deck);
				 }
			 }
		 }
		 //System.out.println("end======front : "+index[0]+"back : "+index[1]);
		 //Print98(deck);
		 System.out.println(cntSum);
	 }
	 
	 public static void Deck3() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int T = Integer.parseInt(in.readLine());
		 for(int t=0; t<T; t++){
			 String fx = in.readLine();
			 int N = Integer.parseInt(in.readLine());
			 String xn = in.readLine().replace("["," ").replace("]"," ").replace(","," ");
			 StringTokenizer st = new StringTokenizer(xn);
			 int deck[] = new int[N+1];
			 int index[] = new int[2];
			 int rflag = 0;    //0: 정배열 , 1: 역배열 
			 int rtnFlag = 0; //0: 문제없음, 1: 에러발생
			 
			 for(int n=0; n<N; n++){
				 int X = Integer.parseInt(st.nextToken()); 
				 Push_Back(deck,index,X);
			 }
			 //Print98(deck,N);  //초기화 배열 출력
			 
			 
			 for(int i=0; i<fx.length(); i++){
				 if(fx.charAt(i)=='R'){
					 if(rflag == 0)
						 rflag = 1;
					 else
						 rflag = 0;
				 }
				 else if(fx.charAt(i)=='D'){
					 if(Deck_Size(deck,index) == 0){
						 rtnFlag = 1;
					 }
					 else if(rflag == 0)
						 Pop_Front(deck, index);
					 else if(rflag == 1)
						 Pop_Back(deck, index);
				 }
			 }
			 if(rtnFlag == 0){
				 System.out.print("[");
				 if(rflag == 0 && !(index[0]==index[1] && deck[index[0]]==0)){
					 for(int i=index[0]; i<=index[1]; i++){
						 System.out.print(deck[i]);
						 if(i != index[1])
							 System.out.print(",");
					 }
				 }
				 else if(rflag == 1 && !(index[0]==index[1] && deck[index[0]]==0)){
					 for(int i=index[1]; i>=index[0]; i--){
						 System.out.print(deck[i]);
						 if(i != index[0])
							 System.out.print(",");
					 }
				 }
				 System.out.print("]");
				 System.out.println("");
			 }
			 else{
				 System.out.println("error");
			 }
		 }
	 }
	 
	 public static void Print98(int[] arr, int N){
		 for(int i=0; i<N; i++){
			 System.out.print(arr[i]+" ");
		 }
		 System.out.println();
	 }
	 
	 public static void Fibo() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 
		 long a = 0;
		 long b = 1;
		 long temp = 0;
		 
		 for(int n=0; n<N; n++){
			 temp = b;
			 b=a+b;
			 a = temp;
		 }
		 System.out.println(a);
	 }
	 
	 public static void Fibo2() throws IOException{ //피사노 주기 F(N)%K = F(N%P)%K
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 long N = Long.parseLong(in.readLine());
		 
		 int a = 0;
		 int b = 1;
		 int temp = 0;
		 int cnt = 0; //주기
		 
		 while(true){  //주기 구하는 부분
			 temp = b%1000000;
			 b = (a+b)%1000000;
			 a = temp;
			 cnt++;
			 if(a==0 && b==1 && a+b==1)
				 break;
		 }
		 
		 for(int n=0; n<N%cnt; n++){
			 temp = b%1000000;
			 b = (a+b)%1000000;
			 a = temp;
		 }
		  
		 System.out.println(a);
	 }
	 
	 public static void Fibo3() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int T = Integer.parseInt(in.readLine());
		 OutputStream os = new BufferedOutputStream(System.out);
		 
		 for(int i=0; i<T; i++){
			 int N = Integer.parseInt(in.readLine());
			 int[][] arr = new int[41][2];
			 
			 arr[0][0] = 1;
			 arr[1][1] = 1;
			 
			 for(int j=2; j<=N; j++){
				 for(int k=0; k<=1; k++){
					 arr[j][k]=arr[j-2][k]+arr[j-1][k];
				 }
			 }
			 os.write((arr[N][0]+" "+arr[N][1]+"\n").getBytes());
		 }
		 os.flush();
		 os.close();
	 }

	 public static void Combine() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 int n = Integer.parseInt(st.nextToken());
		 int r = Integer.parseInt(st.nextToken());
		 int arr[][] = new int[n+1][r+1];
		 int result = 0;
		 result = RecurCombine(arr,n,r);
		 System.out.println(result);
	 }
	 
	 public static void Combine2() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 int n = Integer.parseInt(st.nextToken());
		 int r = Integer.parseInt(st.nextToken());
		 long arr[][] = new long[n+1][r+1];
		 long result = 0;
		 result = RecurCombine2(arr,n,r);
		 System.out.println(result);
	 }
	 
	 public static long RecurCombine2(long[][] arr, int n, int r){
		 if(arr[n][r]>0){
			 return arr[n][r];
		 }
		 if(n==r || r==0){
			 return 1;
		 }
		 arr[n][r]=RecurCombine2(arr,n-1,r-1)+RecurCombine2(arr,n-1,r);
		 return arr[n][r]%1000000007;
	 }
	 
	 public static int RecurCombine(int[][] arr, int n, int r){
		 if(arr[n][r]>0){
			 return arr[n][r];
		 }
		 if(n==r || r==0){
			 arr[n][r]=1;
			 return 1;
		 }
		 arr[n][r]=RecurCombine(arr,n-1,r-1)+RecurCombine(arr,n-1,r);
		 return arr[n][r];
	 }
	 
	 
	 public static void Combine3() throws IOException{  //페르마의 소정리: a^m-1 % m = 1 (a와 m 이 서로소이며, 소수일 때 성립)
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 int N = Integer.parseInt(st.nextToken());
		 int R = Integer.parseInt(st.nextToken());
		 long A = 0;
		 long B = 0;
		 long p = 1000000007;
		 
		 long[] nArr = new long[N+1];
		 nArr[0] = 1;
		 for(int i=1; i<=N; i++){
			 nArr[i]=(nArr[i-1]*i)%p;
		 }
		 
		 A = nArr[N];
		 B = (nArr[R]*nArr[N-R])%p;
		 
		 long index = p-2;
	     long fermatNum = 1;
	     
	     while(index > 0){
	        if(index%2==1){
	            fermatNum *= B;
	            fermatNum %= p;
	        }
	        B = (B*B)%p;
	        index /= 2;
	     }
		 System.out.println(((A%p)*(fermatNum%p))%p);
	 }
	 
	 public static void Factorial() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int[] nArr = new int[N+1];
		 nArr[0]=1;
		 for(int i=1; i<=N; i++){
			 nArr[i]=nArr[i-1]*i;
		 }
		 System.out.println(nArr[N]);
	 }
	 
	 public static void Factorial2() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int num2 = 0;
		 int num5 = 0;
		 int temp = 0;
		 for(int i=1; i<=N; i++){
			 temp=i;
			while(temp%2 == 0 || temp%5 ==0){
				if(temp%2==0){
					temp=temp/2;
					num2++;
				}
				else if(temp%5==0){
					temp=temp/5;
					num5++;
				}
			}
		 }
		 if(num2<num5){
			 System.out.println(num2);
		 }
		 else{
			 System.out.println(num5);
		 }
	 }
	 
	 public static void Combine4() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(in.readLine());
		 int n = Integer.parseInt(st.nextToken());
		 int r = Integer.parseInt(st.nextToken());
		 BigInteger a = new BigInteger("1");
		 BigInteger b = new BigInteger("1");
		 BigInteger[] arr = new BigInteger[n+1];
		 arr[0]=b;
		 arr[1]=b;
		 
		 for(int i=2; i<=n; i++){
			 a=a.add(b);
			 arr[i] = arr[i-1].multiply(a);
		 }
		 b = arr[n].divide((arr[r].multiply(arr[n-r])));
		 System.out.println(b);
	 }
	 
	 public static void Combine5() throws IOException{//n의범위가 안정해져있어 배열의 인덱스로 사용불가. 오버플로우 발생
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 while(true){
			 StringTokenizer st = new StringTokenizer(in.readLine());
			 long n = Long.parseLong(st.nextToken());
			 long r = Long.parseLong(st.nextToken());
			 long result = 1;
			 if(n==0 && r==0)
				 break;
	
			 if(n-r < r)
				 r = n-r;
			  for (long i = 1; i <= r; i++) {
	                result *= n--;
	                result /= i;
	          }
			
			 System.out.println(result);
		 }
	 }
	 
	 public static void Combine6() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int T = Integer.parseInt(in.readLine());
		 for(int i=0; i<T; i++){
			 int N = Integer.parseInt(in.readLine());
			 if(N==0){
				 System.out.println("0");
				 continue;
			 }
			 String[] arr = new String[N];
			 int[] arr2 = new int[N];
			 int k=0;
			 int maxIndex=0;
			 int result = 1;
			 for(int j=0; j<N; j++){
				 StringTokenizer st = new StringTokenizer(in.readLine());
				 String A = st.nextToken();
				 String B = st.nextToken();
				 k = 0;
				 while(true){
					 if(arr[k]==null){
						 arr[k]=B;
						 arr2[k]++;
						 break;
					 }
					 if(arr[k].equals(B)){
					 	 arr2[k]++;
					 	 break;
					 }
					 k++;
				 }
				 if(k>maxIndex)
					 maxIndex=k;
			 }
			 for(int j=0; j<=maxIndex; j++){
				 //System.out.println(arr2[j]);
				 result = result*(arr2[j]+1);
			 }
			 result=result-1;
			 System.out.println(result);
		 }
	 }
	 
	 public static void minCostRGB() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int[][] arr = new int[3][N+1];
		 arr[0][0]=0;
		 arr[1][0]=0;
		 arr[2][0]=0;
		 StringTokenizer st = null;
		 for(int i=1; i<=N; i++){
			 st = new StringTokenizer(in.readLine());
			 arr[0][i]=calMin(arr[1][i-1],arr[2][i-1])+Integer.parseInt(st.nextToken());
			 arr[1][i]=calMin(arr[0][i-1],arr[2][i-1])+Integer.parseInt(st.nextToken());
			 arr[2][i]=calMin(arr[0][i-1],arr[1][i-1])+Integer.parseInt(st.nextToken());
		 }
		 
		 System.out.println(calMin(arr[0][N],arr[1][N],arr[2][N]));
	 }
	 
	 public static int calMin(int a, int b){
		 if(a>=b)
			 return b;
		 else
			 return a;
	 }
	 public static int calMin(int a, int b, int c){
		 int min=a;
		 if(b<min){
			 min=b;
		 }
		 if(c<min){
			 min=c;
		 }
		 return min;
	 }
	 public static int calMax(int a, int b){
		 if(a<=b)
			 return b;
		 else
			 return a;
	 }
	 public static int calMax(int[][] arr, int row){
		 int max=0;
		 for(int i=0; i<arr.length; i++){
			 if(arr[i][row]>max){
				 max=arr[i][row];
			 }
		 }
		 return max;
	 }
	 
	 public static void maxCostTriangle() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = null;
		 int N = Integer.parseInt(in.readLine());
		 int[][] arr = new int[N+1][N+1];
		 arr[0][0]=0;
		 
		 for(int i=1; i<=N; i++){
			 st = new StringTokenizer(in.readLine());
			 for(int j=1; j<=i; j++){
				 arr[j][i]=calMax(arr[j-1][i-1],arr[j][i-1])+Integer.parseInt(st.nextToken());
			 }
		 }
		 System.out.println(calMax(arr,N));
	 }
	 
	 public static void maxCostStair() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int[] score = new int[N+1];
		 int[] sumScore = new int[N+1];
		 for(int i=1; i<=N; i++){
			 score[i] = Integer.parseInt(in.readLine());
		 }
		 sumScore[0]=0;
		 sumScore[1]=score[1];
		 sumScore[2]=score[2]+calMax(sumScore[0],sumScore[1]);

		 for(int i=3; i<=N; i++){
			 sumScore[i]=score[i]+calMax(score[i-1]+sumScore[i-3],sumScore[i-2]);
		 }
		 System.out.println(sumScore[N]);
	 }
	 
	/* public static void minCostNumOne() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int[][] arr = new int[3][N+1];
		 arr[0][0]=N;
		 arr[1][0]=N;
		 arr[2][0]=N;
		 int[] temp = new int[3]; 
		 
		 if(N==1){
			 System.out.println("0");
			 return;
		 }
	
		 for(int i=1; i<=N; i++){
			 for(int j=0; j<3; j++){
				 if(arr[j][i-1]%3==0)
					 temp[j] = arr[j][i-1]/3;
				 else
					 temp[j] = calMin(arr[0][i-1],arr[1][i-1],arr[2][i-1]);
			 }
			 arr[0][i]=calMin(temp[0],temp[1],temp[2]);
			
			 for(int j=0; j<3; j++){
				 if(arr[j][i-1]%2==0)
					 temp[j] = arr[j][i-1]/2;
				 else
					 temp[j] = calMin(arr[0][i-1],arr[1][i-1],arr[2][i-1]);
			 }
			 arr[1][i]=calMin(temp[0],temp[1],temp[2]);
			 
			 arr[2][i]=calMin(arr[0][i-1],arr[1][i-1],arr[2][i-1])-1;
			 
			 if(arr[0][i] == 1 || arr[1][i] == 1 || arr[2][i] == 1){
				 System.out.println(i);
				 break;
			 }
		 }
	 }*/
	 
	 public static void minCostNumOne() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 int N = Integer.parseInt(in.readLine());
		 int[] DP = new int[N+1];
		 DP[0]=-1;
		 for(int i=1; i<=N; i++){
			 DP[i]=DP[i-1]+1;
			if(i%3==0)
				DP[i]=calMin(DP[i],DP[i/3]+1);
			if(i%2==0)
				DP[i]=calMin(DP[i],DP[i/2]+1);
		 }
		 System.out.println(DP[N]);
	 }
	 
	 public static void minCostConstruct() throws IOException{
		 BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = null;
		 int T = Integer.parseInt(in.readLine());
		 int N = 0;
		 int K = 0;
		 int X = 0;
		 int Y = 0;
		 int W = 0;
		 for(int t=0; t<T; t++){
			 st = new StringTokenizer(in.readLine());
			 N = Integer.parseInt(st.nextToken());
			 K = Integer.parseInt(st.nextToken());
			 
			 int[] D = new int[N+1];
			 st = new StringTokenizer(in.readLine());
			 for(int n=1; n<=N; n++){
				 D[n] = Integer.parseInt(st.nextToken());
			 }
			 
			 int[][] XY = new int[N+1][N+1]; //인접행렬
			 for(int k=0; k<K; k++){
				 st = new StringTokenizer(in.readLine());
				 X = Integer.parseInt(st.nextToken());
				 Y = Integer.parseInt(st.nextToken());
				 XY[X][Y]=1;
			 }
			 
			 W = Integer.parseInt(in.readLine());
			 int[] DP = new int[N+1];
			 for(int n=1; n<=N; n++){
				 DP[n] = -1;
			 }
			 System.out.println(calCostConstruct(XY,DP,D,W));
		 }
	 }
	 
	 public static int calCostConstruct(int[][] arr, int[] dp, int[] d, int col){
		 int result = 0;
		 if(dp[col]!=-1){
			 return dp[col];
		 }
		 else{
			 for(int i=1; i<dp.length; i++){
				 if(arr[i][col]==1){
					 result=calMax(result,calCostConstruct(arr,dp,d,i));
				 }
			 }
			 dp[col]=result+d[col];
			 return dp[col];
		 }
	 }
}