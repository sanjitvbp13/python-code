import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        for (int itr = 1; itr <= num; itr++) {
            if (num % itr == 0) {
                System.out.println(itr + "*");
            }
        }
    }
}
