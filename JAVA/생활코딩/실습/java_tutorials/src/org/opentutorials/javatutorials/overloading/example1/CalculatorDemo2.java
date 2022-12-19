package org.opentutorials.javatutorials.overloading.example1;

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
