# overriding (재정의)

부모 클래스도 가지고 있고 자식 클래스도 가지고 있는 메서드를 실행하면 자식 클래스가 가지고 있는 메서드가 실행됨.



## 오버라이딩의 조건

return type이 다르면(부모, 자식의 메서드 형식이 다르면), 이름이 다르면, 매개변수가 다르면 오버라이딩 안됨.



부모와 자식이 같은 로직을 갖고 있을 때 **super** 사용



```java
class Calculator {
    int left, right;
    
    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }
    
    public void sum() {
        System.out.println(this.left + this.right);
    }
    
    public int avg() {
        System.out.println((this.left + this.right) / 2);
    }
}

class SubstractionableCalculator extends Calculator {
    
    public void sum() {
        System.out.println("실행 결과는 " + (this.left + this.right) + "입니다.");
    }
    
	public int avg() {
        return (this.left + this.right)/2;
        // return super.avg();
    }
    
    public void substract() {
        System.out.println(this.left - this.right);
    }
}

public class CalculatorDemo {
    public static void main(String[] args) {
        SubstractionableCalculator c1 = new SubstractionableCalculator();
        c1.setOprands(10, 20);
        c1.sum();
        c1.avg();
        //System.out.println("실행 결과는" + c1.avg());
        c1.substract();
    }
}
```



# overloading

같은 이름, 다른 개수의 매개변수 => 다른 메서드로 인식



```java
class Calculator {
	int left, right;
	int third = 0;
	
	public void setOprands(int left, int right) {
		System.out.println("setOprands(int left, int right)");
		this.left = left;
		this.right = right;
	}
	
	public void setOprands(int left, int right, int third) {
		System.out.println("setOprands(int left, int right, int third)");
		this.left = left;
		this.right = right;
		this.third = third;
	}
	
	public void sum() {
		System.out.println(this.left + this.right + this.third);
	}
	
	public void avg() {
		System.out.println((this.left+this.right+this.third)/3);
	}
}

public class CalculatorDemo {
	
	public static void main(String[] args) {
		
		Calculator c1 = new Calculator();
		c1.setOprands(10, 20);
		c1.sum();
		c1.avg();
		c1.setOprands(10, 20, 30);
		c1.sum();
		c1.avg();
	}
}
```



## 오버로딩의 규칙

```java
public class OverloadingDemo {
	void A () {
		System.out.println("void A()");
	}
	void A (int arg1) {
		System.out.println("void A (int arg1)");
	}
	void A (String arg1){
		System.out.println("void A (String arg1)");
	}
//	int A () {
//		System.out.println("void A()");
//	}
	public static void main(String[] args) {
		OverloadingDemo od = new OverloadingDemo();
		od.A();
		od.A(1);
		od.A("coding everybody");
	}
}
```



## 상속과 오버로딩

```java
public class OverloadingDemo2 extends OverloadingDemo {
	// 오버로딩
    void A (String arg1, String arg2) {
		System.out.println("sub class : void A (String arg1, String arg2)");
	}
    // 오버라이딩
	void A () {
		System.out.println("sub class : void A ()");
	}
	
	public static void main(String[] args) {
		OverloadingDemo2 od = new OverloadingDemo2();
		od.A();
		od.A(1);
		od.A("coding everybody");
		od.A("coding everybody", "coding everybody");
	}
}
```



## overriding VS overloading

오버라이딩 : 부모 클래스의 메소드의 동작방법을 변경

오버로딩 : 같은 이름, 다른 매개변수의 메소드들을 여러개 만들 수 있다.



## +

더 많은 값을 대상으로 연산을 해야 할 때

```java
class Calculator2{
	int[] oprands;
	
	public void setOprands(int[] oprands) {
		this.oprands = oprands;
	}
	
	public void sum() {
		int total = 0;
		for(int value : this.oprands) {
			total += value;
		}
		System.out.println(total);
	}
	
	public void avg() {
		int total = 0;
		for(int value : this.oprands) {
			total += value;
		}
		System.out.println(total/this.oprands.length);
	}
}
public class CalculatorDemo2 {
	public static void main(String[] args) {
		Calculator2 c1 = new Calculator2();
		c1.setOprands(new int[] {10, 20});
		c1.sum();
		c1.avg();
		c1.setOprands((new int[] {10, 20, 30}));
		c1.sum();
		c1.avg();
	}
}
```

