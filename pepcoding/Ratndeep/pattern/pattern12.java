import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        int n = scn.nextInt();
        int a=0;
        int b=1;
        int c=a+b;
        if(n>=1)
            System.out.println(a);
        if(n>=2)
            System.out.println(b+"\t"+c);
        a=b;
        b=c;
        for(int i=3;i<=n;i++){
            for(int j=1;j<=i;j++){
                c=a+b;
                System.out.print(c+"\t");
                a=b;
                b=c;
            }
            System.out.println();
        
        }

    }
}