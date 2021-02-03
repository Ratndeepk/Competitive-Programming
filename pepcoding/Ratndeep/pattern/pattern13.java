import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        //write your code here
        int n = scn.nextInt();
        
        for(int i=0;i<n;i++){
            int pr=1;
            for(int j=0;j<=i;j++){
                System.out.print(pr+"\t");
                int pr1= pr*(i-j)/(j+1);
                pr=pr1;
            }
            System.out.println();
        }
    }
}