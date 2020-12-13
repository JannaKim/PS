package CLASS;

public class FinalEx {
    public static void main(String[] args)
    {
        Final p1 = new Final("950709-2000000", "Janna Kim");
        System.out.printf("%s %s %n", p1.nation, p1.name);

    }

}


public class Final {
    final String nation = "Korean";
    final String ssn; // 이 두개는 한번 값 들어오면 바꿀 수 없도록 하겠다.
    String name;

    //생성자 어케 만들더라
    Final(String ssn, String name){
        this.ssn = ssn;
        this.name = name;
    }

}


