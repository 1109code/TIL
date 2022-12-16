package org.opentutorials.javatutorials.method;

public class MethodDemo1 {
	// 정의
	public static void numbering() {
		int i = 0;
		while (i < 10) {
			System.out.println(i);
			i++;
		}
	}
	// 호출
	public static void main(String[] args) {
		numbering();
		numbering();
		numbering();
	}
}
