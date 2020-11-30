class Hello{
    public static void main(String args[]){
        System.out.println("Hello");
        int year=1, age=14;
        System.out.println("year:"+year+" age:"+age);
        int tmp;
        tmp=year;
        year=age;
        age=tmp;
        System.out.println("year:"+year+" age:"+age);
        int curPos=0;
        int lastPos=-1;

        Date today = new Date();
        System.out.println(today);

        final int MAX = 10000;
        System.out.println(MAX);
        double a = 100L; //또는 ㅣ
        float b = 3.14f;
        //float b = p-1f;
        System.out.println(b);
        int i = 'a';
        System.out.println(i);

        char A='A';
        String names = "Java";
        System.out.println(a+names);

        String name = "Java";
        String is = name+1;
        System.out.println(is);
        System.out.println('a'+7+7); //char 을 연산한 것이므로 97로 변환된다. 
        System.out.println(7+7+"");

    }
}
class Date{
}
// 자바는 문자, 숫자 같이 출력할 때 + 쓴다
/*
변수 명명 규칙:
1. true: 예약어, True: 예약어x
2. 숫자로 시작해선 안된다
3. 특수문자 허용: _, $
4. keywords: final, goto, new, this
5. 권장규칙: 
    클래스 이름은 항상 대문자로 시작
    변수와 메서드는 항상 소문자로 시작
    여러 단어로 이루어진 이름은 단어의 첫글자를 대문자로
    상수의 이름은 모두 대문자로, 여러단어인경우_로 구분

6. 변수 종류: 가본형 8개, 참조형
    * 참조형: C와 달리 참조형 변수간의 연산을 할 수 없다

    기본형: 논리형(boolean), 문자형(char), 정수형(byte, short, int, long)
        실수형(float, double)
    참조형: 8개의 기본형을 제외한 나머지
        *참조형 변수는 타입으로 클래스의 이름을 사용한다.
            새로운 클래스를 작성한다는 것은 새로운 참조형을 추가하는 것이다.
*/
