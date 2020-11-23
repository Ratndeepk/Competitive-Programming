package practice;

import java.util.Arrays;
import java.util.Scanner;

public class LeftRorateArrayByD {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int d = sc.nextInt();
	int arr[] = new int[n];
	for (int i = 0; i < n; i++) {
	    arr[i] = sc.nextInt();
	}
	// if d is greater than n then (d-n) rotations required

	method3(arr, d);
    }

    // Big O(n* d)
    public static void method1(int[] arr, int d) {
	for (int i = 0; i < d; i++) {
	    arr = leftrotate(arr);
	}
	System.out.println(Arrays.toString(arr));
    }

    
    public static int[] leftrotate(int[] arr) {
	int n = arr.length;
	int temp = arr[0];
	for (int i = 1; i < n; i++) {
	    arr[i - 1] = arr[i];
	}
	arr[n - 1] = temp;
	return arr;
    }
    //Big O(n+d)
    public static void method2(int[] arr, int d) {
	int n = arr.length;
	int temp[] = new int[d];
	for (int i = 0; i < d; i++) {
	    temp[i] = arr[i];
	}
	for (int i = d; i < n; i++) {
	    arr[i - d] = arr[i];
	}
	for (int i = 0; i < d; i++) {
	    arr[n - d + i] = temp[i];
	}
	System.out.println(Arrays.toString(arr));
    }
    //Big O(n) recursive soltion
    public static void method3(int[] arr, int d) {
	int n = arr.length;
	arr = reverse(arr, 0, d - 1);
	arr = reverse(arr, d, n - 1);
	arr = reverse(arr, 0, n - 1);
	System.out.println(Arrays.toString(arr));
    }

    public static int[] reverse(int[] arr, int low, int high) {
	while (low < high) {
	    int temp = arr[high];
	    arr[high] = arr[low];
	    arr[low] = temp;
	    low++;
	    high--;
	}
	return arr;
    }
}
