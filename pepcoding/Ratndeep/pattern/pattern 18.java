import java.util.*;

public class Main{

public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);

     // write ur code here
     int n = scn.nextInt();
     int x=1;
     int y=0;

     for(int i=1;i<=n;i++){
         
         for(int j=2;j<=x;j++){
             System.out.print("\t");
         }
         if (i<n/2+1) x++;
         else x--;
         
         
         for(int j=1;j<=n-y;j++){
            if (i<=n/2 && j>1 && i>1 && j<n-y)
                System.out.print("\t");
            else
                System.out.print("*\t");
           
         }
        
         if (i<n/2+1) y+=2;
         else y-=2;
         System.out.println();
     }

 }
}