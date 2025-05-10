import java.util.*;

public class Main {

    public static MagicNumber(long num)
    {
        long reverse=0;
        while(num!=0)
        {
            int dig = (int)(num%10);
            reverse= reverse*10+dig;
            num = num/10;
        }
        
        return reverse;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();// 22
        long original = num;
        int count = 0;
        int sum = 0;
        while (num != 0) {
            num = num / 10;
            count++;
        }
        long pow = (long) Math.pow(10, count - 1);
        num = original;
        while (num != 0) {
            int dig = (int) (num / pow);
            sum = sum + dig;
            num = num % pow;
            pow /= 10;
        }
        long newrev = Reverse(sum);
        long pro = sum * newrev;
        if (pro == original) {
            System.out.println("Magic number");
        } else {
            System.out.println("Not");
        }
    }
}
