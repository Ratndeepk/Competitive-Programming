package practice;

import java.util.Scanner;

public class SubArraySumArray {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int s = sc.nextInt();
	int arr[] = new int[n];
	for (int i = 0; i < n; i++) {
	    arr[i] = sc.nextInt();
	}

	// BigO - O(n)
	method1(arr, s);

    }

    public static void method1(int[] arr, int s) {
	int start = -1, end = -1, i = 0, j = 0, sum = 0;

	while (j < arr.length && sum + arr[j] < s) {
	    sum += arr[j];
	    j++;
	    
	}
	if (s == sum) {
	    System.out.println("Sub array exists init " + i + 1 + " " + j);
	    return;
	}
	while (j < arr.length) {
	    sum += arr[j];
	    while(sum>s) {
		sum -=arr[i];
		i++;
	    }
	    if(s==sum) {
		start = i;
		end = j;
	    }
	    j++;
	}
	if(start != -1 && end != -1) {
	    System.out.println("Sub array exists " + start + " " + end);
	}else {
	    System.out.println("Sub array does not exists");
	}
	
    }
}
