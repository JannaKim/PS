package practiceclass.alparta; //패키지 명: 모두 소문자


public class AlpartaPrj1{
    public static void main(String[] arv) //throws IOException
    {
        Alparta user1 = new Alparta("Minjae","Kim");
        Alparta user2 = new Alparta("Damo");
        System.out.println(user1.getUserName());
        System.out.println(user2.getUserName());
        user1.setUserName("MINJAE","KIM");
        System.out.println(user1.getUserName());
        System.out.println(Alparta.OWNER);
        System.out.println(Alparta.getAlgoList());



    }
}

public class Alparta
{
    static final String OWNER= new String("Janna Kim"); // static final field: 
    private String userName; //instance final field: initialize it in constructor.
    //private: can only call inside the class: username should be fixed at the instance it is created.
    static String getAlgoList()
    {
        return AlpartaAlgo.readAlgoList(); 
    }


    private static class AlpartaAlgo //외부에서 사용할 수 없도록, 클래스 안에서만 private도 될텐데
    {
        private String[] algoList= {"greedy", "backtracking", "binarysearch", "divide&conquer",
        "bfs&dfs", "dijikstra"};
        private static AlpartaAlgo algorithms = new AlpartaAlgo(); //private: cant be used outside.

        private AlpartaAlgo(){}// how to set this class singleton. Restrict it it here

        public static String readAlgoList() // should be static. 밖에서 싱글톤 단일객체 불러올 수 없으므로 static으로 열어놔야함?
        {
            String oneLine="";
            for(String algo: algorithms.algoList)
            {
                oneLine+=algo+" ";
            }
            return "Algorith List: "+oneLine;
        }
        /*
        void addToAlgoList(String newAlgo)
        {
            Array.Resize(ref algoList, algoList.Length + 1);
            array[array.Length - 1] = "new string";

        }
        */
    }
    
    public Alparta(String userName) //constructor 
    { 
        this.userName = userName;

    }

    public Alparta(String firstName, String lastName)//constructor overloading
    {
        this(firstName+" "+lastName); // glue it and carry can ONLY defined in constructor.
    }

    public String getUserName() //(needed)
    {
        return userName;
    }

    public void setUserName(String newName) //method
    {
        this.userName=newName;
        System.out.printf("Your username is changed to %s%n",this.userName);
    }

    public void setUserName(String newFirstName, String newLastName) //method overloading
    {
        this.userName= newFirstName+" "+newLastName;
        System.out.printf("Your username is changed to %s%n",this.userName);
    }



}