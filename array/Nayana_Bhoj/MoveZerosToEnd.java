package practice;

import java.util.Arrays;
import java.util.Scanner;

public class MoveZerosToEnd {
    public static void main(String[] args) {

	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int[] arr = new int[n];
	for (int i = 0; i < n; i++) {
	    arr[i] = sc.nextInt();
	}
	method2(arr);
    }

    public static void method1(int[] arr) {
	int n = arr.length;
	for (int i = 0; i < n; i++) {
	    if (arr[i] == 0) {
		for (int j = i + 1; j < n; j++) {
		    if (arr[j] != 0) {
			int temp = arr[j];
			arr[j] = arr[i];
			arr[i] = temp;
		    }

		}
	    }
	}
	System.out.println(Arrays.toString(arr));
    }

    public static void method2(int[] arr) {
	int n = arr.length;
	int count = 0;
	for (int i = 0; i < n; i++) {
	    if (arr[i] != 0) {
		int temp = arr[count];
		arr[count] = arr[i];
		arr[i] = temp;
		count++;
	    }
	}
	System.out.println(Arrays.toString(arr));
    }
    
    

}
