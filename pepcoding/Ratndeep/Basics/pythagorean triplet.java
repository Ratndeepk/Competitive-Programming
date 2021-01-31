import java.util.*;

public class Main {

    static boolean check(int a, int b, int c) {
        if (a * a == (b * b + c * c))
            return true;
        if (b * b == (c * c + a * a))
            return true;
        if (c * c == (b * b + a * a))
            return true;
        else
            return false;
    }

    public static void main(String[] args) {
        // write your code here 
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(check(a, b, c));



    }
}