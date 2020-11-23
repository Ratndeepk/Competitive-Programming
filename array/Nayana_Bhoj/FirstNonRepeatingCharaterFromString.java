package practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class FirstNonRepeatingCharaterFromString {

    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	String str = sc.nextLine();
	System.out.println(method3(str));
	
    }

    // Big O - O(n^2)
    public static String method1(String str) {
	for (int i = 0; i < str.length(); i++) {
	    boolean isReapted = false;
	    for (int j = 0; j < str.length(); j++) {
		if (str.charAt(i) == str.charAt(j) && (i != j)) {
		    isReapted = true;
		    break;
		}
	    }
	    if (isReapted == false) {
		return (Character.toString(str.charAt(i)));
	    }
	}
	return "-1";

    }

    // Big O - O(n)
    public static String method2(String str) {
	HashMap<Character, Integer> char_counts = new HashMap<>();
	for (int i = 0; i < str.length(); i++) {
	    char c = str.charAt(i);
	    if (char_counts.containsKey(c)) {
		char_counts.put(c, char_counts.get(c) + 1);
	    } else {
		char_counts.put(c, 1);
	    }
	}
	for (int i = 0; i < str.length(); i++) {
	    char c = str.charAt(i);
	    if (char_counts.get(c) == 1) {
		return Character.toString(c);
	    }
	}
	return "-1";

    }
    public static String method3(String str) {
	int[] char_count = new int[26];
	for(char c: str.toCharArray()) {
	    char_count[c-'a']++;
	}
	for(char c: str.toCharArray()) {
	    if(char_count[c-'a']==1)return Character.toString(c);
	}
	return "-1";
    }
}
