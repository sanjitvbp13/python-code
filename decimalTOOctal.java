import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        sc.close();

        int octal = 0, place = 1;

        while (num > 0) {
            int rem = num % 8;
            octal += rem * place;
            place *= 10;
            num /= 8;
        }

        System.out.println(octal);
    }
}
