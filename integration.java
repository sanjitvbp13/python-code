import java.util.*;

public class integration {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        while (num != 0) {
            int digit = (int) (num % 10);
            System.out.println(digit);
            num = num / 10;
        }
    }
}
