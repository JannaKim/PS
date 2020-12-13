package CLASS;

import java.io.*;
import java.util.*;

public class CLASS
{
    public static void main(String[] arv) //throws IOException
    {
        Calculator myCal = new Calculator();


        
        short result1 = myCal.sum(1,(byte)2,(byte)3,(byte)4,(byte)5);
        short result2 = myCal.sum(new byte[] {1, 2, 3});
        System.out.printf("%d %d%n", result1, result2);

        int[] arr = new int[10];
        Arrays.fill(arr, 1, 10, 1);
        for(int el: arr)
        {
            System.out.printf("%d ",el);
        }

        //System.out.println(new int[] {1,2,3,4,5});
        System.out.printf("%n%.10f%n", Calculator.area(10));
        int a = 2;
        double b = 3;
        System.out.printf("%.10f%n", a*b); //서로 다른 타입의 변수간의 연산에서는 자동형변환이 일어난다


        int n = 2;
        int m = 3;
        Area nbyM = new Area();
        Area nbyN = new Area();
        System.out.printf("%d, %d%n",nbyM.area(n,m), nbyN.area(n));

        
        
    }

}

public class Calculator
{
    static double pi= 3.14159265;
    static double area(int r)
    {
        return r*r*pi;
    }
    public short sum(byte ... values)
    {
        byte result=0;
        for(int el: values)
        {
            result+=el;
        }
        return result;

    }

    public short sum(int ... values)
    {
        byte result=0;
        for(int el: values)
        {
            result+=el;
        }
        return result;

    }
    
}







public class Area
{
    public int area(int a)
    {
    return this.area(a, a);
    }

    public int area(int a, int b)
    {
    return a*b;
    }



}
    

