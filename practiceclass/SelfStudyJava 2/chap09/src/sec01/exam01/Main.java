package sec01.exam01;

public class Main {
	public static void main(String[] args) {
	
		A.C c = new A.C();
		System.out.println(c.a);
		A.C.method2();
		/*
		A.B b = a.new B();
		b.field1 = 3;
		b.method1();
		*/
		System.out.println(A.C.field2);
		/*
		A.C c = new A.C();
		c.field1 = 3;
		c.method1();
		A.C.field2 = 3;
		A.C.method2();
		*/
		
		//���� Ŭ���� ��ü ������ ���� �޼ҵ� ȣ��

	}

	/**�ٱ� Ŭ����**/

}

public class A {

	public static class C {
		int a = 4;
		final static int field2=3;
		static void method2() { System.out.println("정적 멤버 클래스 안의 정적메소");}
	}

	public static void method() {
		/**���� Ŭ����**/
		
			class D {
			int field1;
			//static int field2;
			void method1() { System.out.println("local class's method");}
			//static void method2() { }
		}
		D d = new D();
		d.method1();
		
	}
}