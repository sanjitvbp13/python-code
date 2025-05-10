/* */
write a program to check whether it is happy number or not.find the sum of the squares of the digits of the number until it becomes 1 or 4. if reaches 4 it is not a happy number.public class 

ex : 86 8^2+6^2=64+36=100
1^2+0^2+0^2=1 happy number


*/
    
}

import java.util.*;

public class HappyNumber {
    public boolean isHappy(int n) {
        while (n != 1 && n != 4) {
            int num = 0;
            while (n > 0) {
                int r = n % 10;
                num += r * r;
                n = n / 10;
            }
            n = num;
        }
        return n == 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        Solution sol = new Solution();
        if (sol.isHappy(n)) {
            System.out.println(n + " is a Happy Number");
        } else {
            System.out.println(n + " is NOT a Happy Number");
        }
    }
}
