import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        
        int n = scn.nextInt();
        
        for(int i=1;i<=n/2+1;i++){
            for(int j=0;j<=n/2-i+1;j++){
                System.out.print("*	");
            }
            for(int j=0;j<2*i-1;j++)
                System.out.print("	");
            for(int j=0;j<=n/2-i+1;j++){
                System.out.print("*	");
            }
            System.out.println();
        }
        for(int i=1;i<=n/2;i++){
            for(int j=0;j<=i;j++)
                System.out.print("*	");
            for(int j=0;j<n-2*i;j++)
                System.out.print("	");
            for(int j=0;j<=i;j++)
                System.out.print("*	");
            System.out.println();
        }
        // write ur code here

    }
}

    