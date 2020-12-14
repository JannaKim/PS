package practiceclass.selfstudyingjava.sec01exam01;

public class DmbCellPhone extends CellPhone{ //Dmb기능 추가
    //field
    public int channel;

    //constructor
    //외부에서 모델 정보를 받을 수 있도록
    public DmbCellPhone(String model, String color, int channel)
    {
        //model 값은 부모 클래스의 model필드에 저장해본다.
        this.model= model;
        this.color= color;
        this.channel= channel;
    }

    //method
    void turnOnDmb(){ System.out.println("channel"+channel+" is now on.");}
    void changeChannelDmb(int channel){ System.out.println("channel switched to"+channel+".");}
    void turnOffDmb(){ System.out.println("Dmb off.");} 



     
}
