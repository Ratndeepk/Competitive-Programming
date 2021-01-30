import java.util.*;

public class Main {

    public static void main(String[] args) {
        // write your code here  
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count=0;
        int ans=0;
        while(n>0){
            int d=n%10;
            count+=1; 
            n/=10;
            
            int temp=1;
            int count1 = d-1;
            while(count1>0){
                temp*=10;
                count1-=1;
            }
            ans+=count*temp;
        }
        System.out.println(ans);
        
    }
}