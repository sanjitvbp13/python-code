
import java.util.*;

public class countDig {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        long original = num;
        int count = 0;
        while (num != 0) {
            num = num / 10;
            count++;
        }
        long pow = (long) Math.pow(10, count - 1);
        System.err.println(pow);
    }
}
