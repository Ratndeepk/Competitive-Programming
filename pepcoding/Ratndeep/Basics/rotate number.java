import java.util.*;

public class Main {

    public static void main(String[] args) {
        // write your code here  
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int count = 0;
        int temp = n;
        while (temp > 0) {
            count += 1;
            temp /= 10;
        }

        int div = 1;
        int mul = 1;

        k = k % count;
        if (k < 0) {
            k += count;
        }
        for (int i = 1; i <= count; i++) {
            if (i <= k) {
                div *= 10;
            } else {
                mul *= 10;
            }
        }

        System.out.println((n % div) * mul + (n / div));
    }
}