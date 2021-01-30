import java.util.*;

public class Main {

    public static void main(String[] args) {
        // write your code here
        int a = 0;
        int b = 1;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n > 0)
            System.out.println(a);
        if (n > 1)
            System.out.println(b);
        for (int i = 3; i <= n; i++) {
            int c = a + b;
            System.out.println(c);
            a = b;
            b = c;
        }
    }
}