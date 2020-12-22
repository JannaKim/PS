package Java;

public class bitoperator {
    public static void main(String[] arv)
    {
        int a= 8;
        int mask;
        String result="";
        for(int i =5; i>-1;i--){
            mask=1;
            mask=mask<<i;
            if((a&mask)>0){
                result+="1";
            }
            else result+="0";
            
            //result= result+((a&mask)>0)?"1":"0";
        }
        System.out.println(result);
    }
    
}
