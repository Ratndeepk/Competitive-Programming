package practice;

import java.util.Scanner;

public class SmallestPositiveNumberInArray {
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
	int N = (int) Math.pow(10, 6) *2;
	boolean idx[] = new boolean[N];
	for (int i = 0; i < N; i++) {
	    idx[i] = false;
	}
	for (int i = 0; i < arr.length; i++) {
	    if (arr[i] >= 0) {
		idx[arr[i]] = true;
	    } 
	}
	int smallestPositiveNumber = -1;
	for (int i = 1; i < arr.length; i++) {
	    if(idx[i] == false) {
		smallestPositiveNumber = i;
		break;
	    }
	}
	System.out.println(smallestPositiveNumber);
    }
}
