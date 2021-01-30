import java.util.*;

public class pattern {

    public static void main(String[] args) {
        // Write your code here
        for (int i=0;i<5;i++){
            System.out.print("*");
        }
        System.out.println();
        int count=3;
        for (int i=0;i<3;i++){
            for(int j=0;j<count;j++){
                System.out.print(" ");
            }
            System.out.println("*");
            count-=1;
        }
        for (int i=0;i<5;i++){
            System.out.print("*");
        }
        System.out.println();
    }
}