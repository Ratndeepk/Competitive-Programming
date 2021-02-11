import java.util.*;

public class Main{

public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);

     // write ur code here
     int n = scn.nextInt();
     for(int i=1;i<=n;i++){
         for(int j=1;j<=n;j++){
            if(i==1){
                if(j==n || j<=n/2+1)
                    System.out.print("*\t");
                else
                    System.out.print("\t");
             }
             
             else if(i==n){
                if(j==1 || j>=n/2+1)
                    System.out.print("*\t");
                else
                    System.out.print("\t"); 
                 
             }
             else if(i<=n/2){
                    if(j==n/2+1 || j==n)
                        System.out.print("*\t");
                    else
                        System.out.print("\t");
             }
             else if(i==n/2+1){
                 System.out.print("*\t");
                 
             }
             else{
                    if(j==n/2+1 || j==1)
                        System.out.print("*\t");
                    else
                        System.out.print("\t");
                 
             }
             
             
         }
         System.out.println();
     }

 }
}