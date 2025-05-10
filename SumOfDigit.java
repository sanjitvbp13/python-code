import java.util.Scanner;

public class SumOfDigit {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        int sum = 0;

        while (num != 0) {
            int digit = (int) (num % 10);
            sum += digit;
            num = num / 10;
        }

        System.out.println("Sum of digits: " + sum);
    }
}
