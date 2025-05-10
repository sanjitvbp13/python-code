/*
 1+2+5=8(sum of factors)","6":1}'> find wheather the given two number are
 amicable pair or not .
 if sum of factor of first numner equald to the 2nd number as well as sum of
 factor of 2nd number its amicable .
 * 
 NOTE : dont include the number as factor for finding sum of factor i.e , 10->
 1+2+5=8 (sum of factor)
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int sum1 = new nextInt();
        int sum2 = new nextInt();
        int sum1 = 0, sum2 = 0;
        int min = Math.mim(num1, sum2);
        int max = Math.max(num1, num2);
        for (int itr1 = 1; itr1 <= max / 2; itr1++) {
            if (min % itr1 == 0 && itr1 <= min / 2) {
                sum1 += itr1;

            }
            if (max % itr1 == 0) {
                sum2 += itr1;
            }
        }
        if (sum == num2 && sum2 == num2) {
            System.out.println("amicable");
        } else {
            System.out.println("not amicable");
        }
    }

}
