package practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class MinimumWindowSubstring {
    public static void main(String[] a) {
	String str = "ADOBECODEBANC";
	String pattern = "ABC";
	findSubString(str, pattern);
    }

    // BruteForce
    public static void minWindow(String searchString, String t) {
	int n = searchString.length();

	int minWindowLengthSeenSoFar = Integer.MAX_VALUE;
	String minWindow = "";

	for (int left = 0; left < n; left++) {
	    for (int right = left; right < n; right++) {
		String windowSnippet = searchString.substring(left, right + 1);

		boolean windowContainsAllChars = stringContainsAllCharacters(windowSnippet, t);

		if (windowContainsAllChars && windowSnippet.length() < minWindowLengthSeenSoFar) {
		    minWindowLengthSeenSoFar = windowSnippet.length();
		    minWindow = windowSnippet;
		}
	    }
	}

	// return minWindow;
	System.out.println(minWindow);
    }

    public static boolean stringContainsAllCharacters(String searchString, String t) {
	Map<Character, Integer> requiredCharacters = new HashMap<Character, Integer>();

	for (int i = 0; i < t.length(); i++) {
	    int occurrencesOfCharacter = requiredCharacters.getOrDefault(t.charAt(i), 0);

	    requiredCharacters.put(t.charAt(i), occurrencesOfCharacter + 1);
	}

	for (int i = 0; i < searchString.length(); i++) {
	    char curChar = searchString.charAt(i);

	    if (requiredCharacters.containsKey(curChar)) {
		// Calculate what the new occurrence count will be
		int newOccurrenceCount = requiredCharacters.get(curChar) - 1;

		/*
		 * If we have satisfied all of the characters for this character, remove the key
		 * from the hashtable.
		 * 
		 * Otherwise, just update the mapping with 1 less occurrence to satisfy for
		 */
		if (newOccurrenceCount == 0) {
		    requiredCharacters.remove(curChar);
		} else {
		    requiredCharacters.put(curChar, newOccurrenceCount);
		}
	    }
	}

	/*
	 * If we satisfied all characters the the required characters hashtable will be
	 * empty
	 */
	return requiredCharacters.isEmpty();

    }

    // Optimized method
    static final int no_of_chars = 256;

    public static void findSubString(String str, String pat) {
	int len1 = str.length();
	int len2 = pat.length();

	// check if string's length is less than pattern's
	// length. If yes then no such window can exist
	if (len1 < len2) {
	    System.out.println("No such window exists");
	    // return "";
	}

	int hash_pat[] = new int[no_of_chars];
	int hash_str[] = new int[no_of_chars];

	// store occurrence ofs characters of pattern
	for (int i = 0; i < len2; i++)
	    hash_pat[pat.charAt(i)]++;

	int start = 0, start_index = -1, min_len = Integer.MAX_VALUE;

	// start traversing the string
	int count = 0; // count of characters
	for (int j = 0; j < len1; j++) {
	    // count occurrence of characters of string
	    hash_str[str.charAt(j)]++;

	    // If string's char matches with pattern's char
	    // then increment count
	    if (hash_pat[str.charAt(j)] != 0 && hash_str[str.charAt(j)] <= hash_pat[str.charAt(j)])
		count++;

	    // if all the characters are matched
	    if (count == len2) {
		// Try to minimize the window i.e., check if
		// any character is occurring more no. of times
		// than its occurrence in pattern, if yes
		// then remove it from starting and also remove
		// the useless characters.
		while (hash_str[str.charAt(start)] > hash_pat[str.charAt(start)] || hash_pat[str.charAt(start)] == 0) {

		    if (hash_str[str.charAt(start)] > hash_pat[str.charAt(start)])
			hash_str[str.charAt(start)]--;
		    start++;
		    //System.out.println("j " + j + " start " + start);
		}
		
		// update window size
		int len_window = j - start + 1;
		if (min_len > len_window) {
		    min_len = len_window;
		    start_index = start;
		}
	    }
	}

	// If no window found
	if (start_index == -1) {
	    System.out.println("No such window exists");
	    // return "";
	}

	// Return substring starting from start_index
	// and length min_len
	System.out.println(str.substring(start_index, start_index + min_len));
    }

    public void method1(String str, String pattern) {
	int[] ascii_str = new int[26];
	int[] ascii_pattern = new int[26];
	for (char c : pattern.toCharArray()) {
	    ascii_pattern[c - 'A']++;
	}
	System.out.println(Arrays.toString(ascii_pattern));
	System.out.println(ascii_pattern[str.charAt(0) - 'A']);
	/*
	 * int count = 0; int patternCount = 0;
	 * 
	 * for (int i = 0; i < str.length(); i++) { for (int j = i; j < str.length();
	 * j++) { ascii_str[str.charAt(i)-'A']++; if(ascii_str[str.charAt(i)-'A'] ==
	 * ascii_pattern[str.charAt(i)-'A']) { count++; patternCount++; } } }
	 */
    }
}
