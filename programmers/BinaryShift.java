package programmers;

public class BinaryShift {
    public static void main(String[] arv)
    {
        String result="";
        int mask;
        int n=30;
        for(int i =5; i>-1;i--){
            mask=1;
            mask=mask<<i;

            result=result+((10&mask)>0)?"1":"0";



        }
        System.out.println(result);
    }

    
    
}
