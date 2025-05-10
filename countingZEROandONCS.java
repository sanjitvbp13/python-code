complete the function count_zero_ones(),which recevies number if elements

sample ip:5 1 1 1 0 0

sample o/p:zc=2 oc=3

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int zc = 0, oc = 0;
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] == 0) {
                zc++;
            } else if (arr[i] == 1) {
                oc++;
            }
        }

        System.out.println("zc= " + zc);
        System.out.println("oc= " + oc);
    }
}
