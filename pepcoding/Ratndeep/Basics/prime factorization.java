import java.util.*;

public class Main {
    
    
    static boolean prime(int a){
        for(int i=2;i*i<=a;i++){
            if(a%i==0){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        // write your code here  
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int div=2;
        while(n>1){
            if(n%div==0 && prime(div)){
                n/=div;
                System.out.print(div);
                System.out.print(" ");
            }
            else{
                div+=1;
            }
        }
        System.out.println();
    }
}