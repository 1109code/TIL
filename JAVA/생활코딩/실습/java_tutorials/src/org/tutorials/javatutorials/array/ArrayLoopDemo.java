package org.tutorials.javatutorials.array;

public class ArrayLoopDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] members = { "최진혁", "최유빈", "한아람" };
		for (int i = 0; i < members.length; i++) {
			String member = members[i];
			System.out.println(member + "이 상담을 받았습니다.");
		}
	}

}
