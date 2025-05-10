/*
Given a number , check whether the number divides completely or not . if the number divides completely then print the digit and stop
the process if not print -1.
constraints:
1 <=N <=10^9
 
Sample input :
    6732632563
Sample output:


*/

import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        long ori = num, count = 0;
        while (num != 0) {
            num = num / 10;
            count++;
        }
        long pow = (int) Math.pow(10, count - 1);
        num = ori;
        int flag = 0;
        while (pow != 0) {
            int dig = (int) (num / pow);
            System.out.println(dig);
            if (ori % dig == 0) {
                flag = 1;
                System.out.println(dig);
                break;
            }
            num = num % pow;
            System.out.println(num);
            pow /= 10;
        }
        if (flag == 0) {
            System.out.println("-1");
        }
    }
}
