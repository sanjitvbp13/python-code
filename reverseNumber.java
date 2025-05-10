/*
find the reverse number of given number
input format :
    Accept an integer number
output format:
    print the reverse number
constraints:
    1 <= input <= 10^15
sample input:
    12345
output:
    54321


explation :
12345%10=4
5*10+4=54
1234/10=123

123%10=3
54*10+3=543
123/10=12

12%10=2
543*10+2=5432
12/10=1

1%10=1
5432*10+1=54321
1/10=0
 */

import java.util.*;

public class reverseNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        long pow = 1;
        long reverse = 0;
        while (pow < num) {

            int dig = (int) (num / pow) % 10;
            reverse = reverse * 10 + dig;
            pow *= 10;
        }
        System.err.println(reverse);
    }
}
