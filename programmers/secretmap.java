package programmers;

    public class secretmap {
        public static String Binary(int a, int n){

            int mask;
            String result="";
            for(int i =n-1; i>-1;i--){
                mask=1;
                mask=mask<<i;
                /*
                if((a&mask)>0){
                    result+="1";
                }
                else result+="0";
                */
                result+=((a&mask)>0)?"1":"0";
            }
            return result;
    
        }
        public static String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
    
        for(int i=0;i<n;i++)
        {
            String binA= Binary(arr1[i],n);
            String binB= Binary(arr2[i],n);
    
            String line= "";
            for(int j=0; j<n;j++)
            {
    
                if(binA.substring(j,j+1).equals("1") || binB.substring(j,j+1).equals("1") )
                    line+="#";
                else line+=" ";
    
            }
            answer[i]=line;
        }
        return answer;
    }
    public static void main(String[] arv)
    {
        String[] mp= solution(5, new int[]{9,20,28,18,11}, new int[]{30,1,21,17,28});
        for(int i=0;i<5;i++)
        {
            System.out.println(mp[i]);
        }
    }
    
}

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        int[][] mp= new int[n][n];
        String[] answer = new String[n];
        
        for(int i=0;i<n;i++)
        {
            //객체의 원시값을 반환한다.
            String binA= String.valueOf(Integer.toBinaryString(arr1[i]));
            String binB= String.valueOf(Integer.toBinaryString(arr2[i]));
            String line= "";
            for(int j=0; j<n;j++)
            {
                // string으로 하지 말기

                if(binA.substring(j,1).equals("1") || binB.substring(j,1).equals("1") )
                    line+="#";
                else line+=" ";

            }
            answer[i]=line;
        }
        return answer;
    }
}

//public static StringBuilder sb= new StringBuilder();
/*
홍민식 to Everyone (1:26 PM)
public static void main(String[] args) {
		int arr1[] = {46, 33, 33, 22, 31, 50};
		int arr2[] = {27, 56, 19, 14, 14, 10};
		solution(6, arr1, arr2);
	}
	
	public static String[] solution(int n, int[] arr1, int[] arr2) {
		String[] answer = new String[n];

        for (int i = 0; i < n; i++) {
            int num = arr1[i] | arr2[i];
            String s = String.valueOf(Integer.toBinaryString(num));
            String result = "";
            for (int k = 0; k < s.length(); k++) {
                if (s.charAt(k) == '1') {
                    result += "#";
                } else {
                    result += " ";
                }
            }
            for (int j = 0; j < n - s.length(); j++) {
                result = " " + result;
            }
            System.out.println(result);
            answer[i] = result;
        }
        return answer;
    }
    */