import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        int n = scn.nextInt();
        int val=1;
        for(int i=1;i<=n;i++){
            if(i==n/2+1){
                for(int j=1;j<=n/2;j++)
                    System.out.print("*\t");
            }
            else{
                for(int j=1;j<=n/2;j++)
                    System.out.print("\t");
                 
            }
            for(int j=1;j<=val;j++){
                System.out.print("*\t");
            }
            if (i<=n/2)val++;
            else val--;
            System.out.println();
        }

    }
}