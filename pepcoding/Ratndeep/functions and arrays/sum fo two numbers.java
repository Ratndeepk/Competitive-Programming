import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    // write your code here
    Scanner sc = new Scanner(System.in);
    int n1 = sc.nextInt();
    int[] arr = new int[n1];
    for(int i=0;i<n1;i++)
        arr[i] = sc.nextInt();
    
    int n2 = sc.nextInt();
    int[] arr1 = new int[n2];
    for(int i=0;i<n2;i++)
        arr1[i]=sc.nextInt();
        
    
    
    int[] sum = new int[n1>n2?n1:n2];
    int c=0;
    int i=n1-1;
    int j = n2-1;
    int k = sum.length-1;
    
    while (k>=0){
        int d = c;
        if(i>=0)
            d+=arr[i];
        if(j>=0)
            d+=arr1[j];
        sum[k] = d%10;
        c = d/10; 
        i--;
        j--;
        k--;
        
    }
    if(c!=0) System.out.println(1);
    for(int val:sum)
        System.out.println(val);
 }

}