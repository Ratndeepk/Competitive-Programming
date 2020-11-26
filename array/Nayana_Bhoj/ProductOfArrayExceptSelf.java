package practice;

import java.util.Arrays;
import java.util.Scanner;

public class ProductOfArrayExceptSelf {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int arr[] = new int[n];
	for (int i = 0; i < n; i++) {
	    arr[i] = sc.nextInt();
	}
	method1(arr, n);
	method2(arr, n);
	method3(arr);

    }

    public static void method3(int[] nums) {
	// Array Length
	int len = nums.length;

	// Declare three arrays
	int[] left = new int[len];
	int[] right = new int[len];
	int[] ans = new int[len];

	left[0] = 1;

	for (int i = 1; i < nums.length; i++) {
	    left[i] = left[i - 1] * nums[i - 1];
	}

	right[len - 1] = 1;
	for (int i = len - 2; i >= 0; i--) {
	    right[i] = right[i + 1] * nums[i + 1];
	}

	for (int i = 0; i < len; i++) {
	    ans[i] = left[i] * right[i];
	}
	System.out.println(Arrays.toString(ans));
	// return ans;
    }

    public static void method2(int[] arr, int n) {
	int[] left = new int[n];
	int[] result = new int[n];
	int temp_left = 1;
	int zeros = 0;
	int product = 1;
	for (int i : arr) {
	    if (i == 0) {
		zeros++;
	    }
	}
	for (int i = 0; i < n; i++) {

	    if (arr[i] == 0) {
		// current element is 0 but there is another 0 elsewhere
		if (zeros > 1)
		    left[i] = 0;
		// current element is 0 and there are no other 0s
		else
		    left[i] = temp_left;
	    } else {
		// current element is nonzero but there is a 0 elsewhere
		if (zeros > 0)
		    left[i] = 0;
		// current element is nonzero and there are no 0s
		else {
		    left[i] = temp_left * arr[i];
		    temp_left = left[i];
		}
	    }

	}

	result[n - 1] = left[n - 2];
	product = arr[n - 1];
	for (int i = n - 2; i > 0; i--) {
	    result[i] = product * left[i - 1];
	    product = product * arr[i];
	}
	result[0] = product;
	System.out.println(Arrays.toString(result));
    }

    public static void method1(int[] arr, int n) {
	int[] left = new int[n];
	int[] right = new int[n];
	int[] result = new int[n];
	int temp_left = 1;
	int zeros = 0;
	for (int i : arr) {
	    if (i == 0) {
		zeros++;
	    }
	}

	for (int i = 0; i < n; i++) {

	    if (arr[i] == 0) {
		// current element is 0 but there is another 0 elsewhere
		if (zeros > 1)
		    left[i] = 0;
		// current element is 0 and there are no other 0s
		else
		    left[i] = temp_left;
	    } else {
		// current element is nonzero but there is a 0 elsewhere
		if (zeros > 0)
		    left[i] = 0;
		// current element is nonzero and there are no 0s
		else {
		    left[i] = temp_left * arr[i];
		    temp_left = left[i];
		}
	    }

	}
	System.out.println("left " + Arrays.toString(left));
	int temp_right = 1;
	for (int i = n - 1; i >= 0; i--) {
	    if (arr[i] == 0) {
		// current element is 0 but there is another 0 elsewhere
		if (zeros > 1)
		    right[i] = 0;
		// current element is 0 and there are no other 0s
		else
		    right[i] = temp_right;
	    } else {
		// current element is nonzero but there is a 0 elsewhere
		if (zeros > 0)
		    right[i] = 0;
		// current element is nonzero and there are no 0s
		else {
		    right[i] = temp_right * arr[i];
		    temp_right = right[i];
		}
	    }

	}
	System.out.println("right " + Arrays.toString(right));
	result[0] = right[1];
	result[n - 1] = left[n - 2];
	for (int i = 1; i < (n - 1); i++) {
	    result[i] = left[i - 1] * right[i + 1];
	}
	System.out.println(Arrays.toString(result));
    }

}
