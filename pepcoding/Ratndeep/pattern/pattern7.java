import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        int n = scn.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <=i; j++)
                if(i==j)
                    System.out.println("*\t");
                else
                    System.out.print("\t");
                
        }

    }
}