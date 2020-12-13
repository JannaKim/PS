package practiceclass.selfstudyingjava.sec01exam01;

import practiceclass.selfstudyingjava.sec01exam01.*;


public class DmbCelPhoneEx {
    public static void main(String[] args)
    {
        DmbCellPhone myDmb = new DmbCellPhone("Java", "Pink", 3);
        System.out.println(myDmb.model);
        myDmb.powerOn();
        myDmb.bell();
        myDmb.sendVoice("Hello");
        myDmb.receiveVoice("Bye");
        myDmb.hangUp();

        myDmb.turnOnDmb();
        myDmb.changeChannelDmb(4);
        myDmb.turnOffDmb();
    }
    
}
