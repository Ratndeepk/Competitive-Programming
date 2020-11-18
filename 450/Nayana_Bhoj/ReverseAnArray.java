package loveBabar450;

public class ReverseAnArray {

    public static void main(String[] args) {
	/*** Reverse an array ***/
	int arr[] = { 4, 5, 1, 2, 3 };
	System.out.println("Array before ");
	printArray(arr, 5);
	int[] result = approach1(arr);
	System.out.println("Array after reverse ");
	printArray(result, 5);
    }

    public static int[] approach1(int[] arr) {
	int[] result = new int[arr.length];
	int counter = 0;
	for (int i = arr.length; i < 0; i--) {
	    result[counter] = arr[i];
	    counter++;
	}
	return result;

    }

    static void printArray(int arr[], int size) {
	for (int i = 0; i < size; i++)
	    System.out.print(arr[i] + " ");

	System.out.println();
    }

}
