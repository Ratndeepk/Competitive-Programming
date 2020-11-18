package practice;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class FirstRepeatingElementInArray {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int arr[] = new int[n];
	for (int i = 0; i < n; i++) {
	    arr[i] = sc.nextInt();
	}
	// BigO - O(2n)
	method1(arr);
	// BigO - O(n)
	method2(arr);

    }

    public static void method1(int[] arr) {
	int N = (int) Math.pow(10, 6);
	int idx[] = new int[N];
	for (int i = 0; i < N; i++) {
	    idx[i] = -1;
	}
	int minidx = Integer.MAX_VALUE;
	for (int i = 0; i < arr.length; i++) {
	    if (idx[arr[i]] != -1) {
		minidx = Math.min(minidx, idx[arr[i]]);
	    } else {
		idx[arr[i]] = i;
	    }
	}
	if (minidx == Integer.MAX_VALUE) {
	    System.out.println(-1);
	} else {
	    System.out.println(minidx);
	}
    }

    public static void method2(int[] arr) {
	int min = -1;
	Set<Integer> myset = new HashSet<>();

	for (int i = (arr.length - 1); i >= 0; i--) {
	    if (myset.contains(arr[i])) {
		min = i;
	    } else {
		myset.add(arr[i]);
	    }
	}
	System.out.println(min);
    }
}
