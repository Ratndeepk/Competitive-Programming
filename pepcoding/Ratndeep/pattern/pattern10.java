import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        int n = scn.nextInt();
        int out=n/2;
        int in = -1;
        for(int i=1;i<=n;i++){
            
            for(int j=1;j<=out;j++)
                System.out.print("\t");
            if(i==1 || i==n)
                System.out.println("*\t");
                
            else{
                System.out.print("*\t");
                
                for(int j=1;j<=in;j++)
                    System.out.print("\t");
            }
            if(i!=1 && i!=n)
                System.out.println("*\t");
                
            if (i<=n/2){
                out-=1;
                in+=2;
            }
            else{
                out+=1;
                in-=2;
            }
        }

    }
}