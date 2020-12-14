package CLASS;

public class SingletonEx {
    public static void main(String[] arv)
    {
        Singleton obj1 = Singleton.getInstance();

    }
}




public class Singleton { //객체가 하나만 만들어지도록
    private static Singleton singleton = new Singleton();

    private Singleton() {} // 이렇게 두 개 해줘야 싱글톤 된다.

    static Singleton getInstance(){
        return singletone; // 번지가 저장 돼 있다.
    }

    
}
