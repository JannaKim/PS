package programmers;

public class secretmap {
    
}

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        int[][] mp= new int[n][n];
        String[] answer = new String[n];
        
        for(int i=0;i<n;i++)
        {
            String binA= Integer.toBinaryString(arr1[i]);
            String binB= Integer.toBinaryString(arr2[i]);
            String line= "";
            for(int j=0; j<n;j++)
            {
                
                if(binA[j].equals("1") || binB[j].equals("1") )
                    line+="#";
                else line+=" ";
            }
            answer[i]=line;
        }
        return answer;
    }
}