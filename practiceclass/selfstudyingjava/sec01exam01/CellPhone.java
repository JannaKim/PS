package practiceclass.selfstudyingjava.sec01exam01;

public class CellPhone {
    //Field
    String mode1;
    String color;

    //Constructor
    //default 생성자.
    public CellPhone(){}//와 같은 의미.

    //Method 
    void powerOn(){System.out.println("Turn on");}
    void powerOff(){System.out.println("Turn off");}
    void bell(){System.out.println("Bell Rings");}
    void sendVoice(String message){System.out.println("You: "+message);}
    void receiveVoice(String message){System.out.println("Caller: "+message);}
    void hangUp(){System.out.println("Hang up");}

    
}
