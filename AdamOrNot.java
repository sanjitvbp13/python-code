/*find the whether the given number is adam or not . the squre of the given number is equal to the reverse of the squre of the reverse of the given number
for example , consider the input 12.
squre(12)   = 144
reverse(/squre (reverse(12))) = 144
*/

import java.util.*;

public class AdamOrNot {
    public static long Reverse(long num) {
        long reverse = 0;
        while (num > 0) {
            reverse = reverse * 10 + (num % 10);
            num = num / 10;
        }
        return reverse;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong(); // Use nextLong to support large numbers
        long square = num * num;
        long rev = Reverse(num);
        long revSquare = rev * rev;
        long revOfRevSquare = Reverse(revSquare);

        if (square == revOfRevSquare) {
            System.out.println("Adam");
        } else {
            System.out.println("Not Adam");
        }
    }
}
