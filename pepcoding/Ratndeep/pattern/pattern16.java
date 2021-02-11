import java.util.*;

public class Main{

public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);

     // write ur code here
     int n =scn.nextInt();
     int c=2;
     for(int i=1;i<=n;i++){
         for(int j=1;j<=i;j++){
             System.out.print(j+"\t");
         }
         for(int j=1;j<2*n-c;j++){
             System.out.print("\t");
         }
         c+=2;
         int loop=i;
         if (loop==n){loop-=1;}
         int val=loop;
         for(int j=1;j<=loop;j++){
             System.out.print(val+"\t");
             val--;
         }
         System.out.println();
     }

 }
}