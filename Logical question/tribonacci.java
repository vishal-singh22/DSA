import java.util.*;
class Solution {
    public static int tribonacci(int n){
        if(n<=2){
            return (n==0)?0:1;
        }
        int prev0=0;
        int prev1=1;
        int prev2=1;
        int sum=0;
        for(int i=3;i<=n;i++){
            sum = prev0+prev1+prev2;
            prev0=prev1;
            prev1=prev2;
            prev2=sum;
        }
        return sum;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the value");
        int n=sc.nextInt();
        int res=tribonacci(n);
        System.out.println("tribonacci searies is : "+res);
        
    }
}