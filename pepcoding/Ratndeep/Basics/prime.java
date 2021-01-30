import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        int t = scn.nextInt();
        while (t > 0) {
            int flag = 0;
            int n = scn.nextInt();
            for (int i = 2; i * i <= n; i++) {
                if (n % i == 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                System.out.println("prime");
            } else
                System.out.println("not prime");
            t -= 1;

        }

    }
}