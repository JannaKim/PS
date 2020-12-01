

package Java;
import java.util.*;
public class From36p {
    public static void main(String args[]){
        int age = 26;
        System.out.printf("Janna is %d years old.%n",age);
        byte b= 1;
        short s= 2;
        char c= 'A';
        // char c= ''; error. 문자 리터럴은 반드시 하나의 문자가 있어야 한다.
        int finger= 'A'; //넓은 타입에 좁은 타입의 값을 저장하는 것은 허용된다.
        long big= 1_000_000_000L;
        long hex= 0xFFFF_FFFF_FFFF_FFFFL; //16진수임을 표시하기 위해 접두사 0x붙인다.

        int octNum= 010; //8진수임을 표시하기 위해 접두사 0 붙인다
        int hexNum= 0x10;
        int binNum= 0b10;

        System.out.printf("b=%d%n",b);
        System.out.printf("s=%d%n",s);
        System.out.printf("c=%c, %d%n",c,(int)c); // 자바는 char타입 값을 %d로 출력하기 위해 (int)로 형변환 해줘야 한다.

        // printf 안에서 연산 안되나?
        System.out.printf("finger=[%05d]%n",finger); // -5 붙이면 5개 공간만들고 왼쪽정렬, 나머지는 공백. 05d 하면 나머지는 0.. 다른 숫자나 문자는 안된다.
        System.out.printf("finger=%5d%n",finger);
        System.out.printf("finger=%-5d%n",finger);

        System.out.printf("big=%d%n",big);
        System.out.printf("hex=%#x%n",hex);

        System.out.printf("octNum=%#o %d%n",octNum, octNum);
        System.out.printf("hexNum=%#x %d%n",hexNum, hexNum); // 16진수 지시자는 %x. %0x아님
        System.out.printf("binNum=%s %d%n", Integer.toBinaryString(binNum), binNum); //0b는 표현안되는 듯



        // 5개 공간 만들고, 왼쪽정렬, 나머지 *?

        String url= "www.codechobo.com";
        System.out.printf("%.8s%n",url); // 왼쪽에서 8개만 출력. 오른쪽은?
        System.out.printf("%-20s%n",url);

        float f1= .1f;
        float f2= 1e1f;
        float f3= 3.14e3f;
        //float f4= 3.1415926535f;
        double f4= 3.1415926535;
        System.out.printf("%f %e %g%n",f1, f1, f1);
        System.out.printf("%f %e %g%n", f2, f2, f2);
        System.out.printf("%f %e %g%n",f3, f3, f3);
        System.out.printf("%20.7f%n",f4);

        double d = 1.23456789;
        System.out.printf("d=%f %.10f%n",d,d);


        Scanner scanner= new Scanner(System.in);

        System.out.print("입력:");
        String input= scanner.nextLine();
        int num= Integer.parseInt(input);

        System.out.println(input);
        System.out.println(num);
        System.out.printf("%s%n",input);
        System.out.printf("%d%n",num);



    }
    
}
