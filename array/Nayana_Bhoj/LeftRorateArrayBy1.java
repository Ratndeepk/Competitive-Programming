package practice;

import java.util.Arrays;
import java.util.Scanner;

public class LeftRorateArrayBy1 {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int arr[] = new int[n];
	for (int i = 0; i < n; i++) {
	    arr[i] = sc.nextInt();
	}
	method1(arr);
    }
    
    public static void method1(int[] arr) {
	int n = arr.length;
	int temp = arr[0];
	for(int i=1;i<n;i++) {
	    arr[i-1] = arr[i];
	}
	arr[n-1] = temp;
	System.out.println(Arrays.toString(arr));
    }
}
