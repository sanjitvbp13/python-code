
/* 
 given harshad number or not
harshad number  if the number is divisible by the sum of its digits.
input format :
Accept an integer number
output format:
if the number is harshad number print "yes" else "no"

sample input:
510
output:
yes

 */
import java.util.*;

public class harshadNumber {
    public static void main(string[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number:");
        int num = sc.nextInt();
        int sum = 0, temp = num;

        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }

        if (num % sum == 0) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}