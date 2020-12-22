package sec01.exam01;

public class Main {
	public static void main(String[] args) {
		/*
		A a = new A();

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
		//a.method();
	}

	/**�ٱ� Ŭ����**/

}

public class A {

	public static class C {
		final static int field2=3;
		static void method2() { }
	}

	public static void method() {
		/**���� Ŭ����**/
		/*
			public static class D {
			public static int field1;
			//static int field2;
			public static void method1() { }
			//static void method2() { }
		}
		*/
	}
}