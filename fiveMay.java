// accept an integer and print number along with its sign(without using
// condition statement)
// ip= -10
// op = 10

/*
 * Q2: give an integer value , check the given input id dividible by 3 . if it
 * is divisible print the message "the number is dividible by 3 "
 * if not print "the number is not dividible by 3 and give a remainder"
 * ip = 15
 * op = the number is dividible by 3
 * ip = 16
 * op = the number is not dividible by 3 and give a remainder 1
 */

// public class five_may {
// public static void main(String[] args) {
// int num = -10;
// System.out.println(num + (num < 0 ? " is negative" : "is positive"));
// }
// }

/*
 * given an interger value , if it is divisible by 3 print "HI", if is divisible
 * by 5 print "HELLO" if it is divisible by both print "HIHELLO",else print NONE
 * "
 * 
 * 
 * 
 * import java.util.Scanner;
 * 
 * public class fiveMay {
 * public static void main(String[] args) {
 * Scanner scanner = new Scanner(System.in);
 * 
 * 
 * System.out.print("Enter an integer: ");
 * int num = scanner.nextInt();
 * 
 * 
 * if (num % 3 == 0 && num % 5 == 0) {
 * System.out.println("HIHELLO");
 * } else if (num % 3 == 0) {
 * System.out.println("HI");
 * } else if (num % 5 == 0) {
 * System.out.println("HELLO");
 * } else {
 * System.out.println("NONE");
 * }
 * 
 * scanner.close();
 * }
 * }
 * 
 */

/*
 * input a given specific number and check wheter the date is vaild or not. year
 * will be in range 1900 to 9999
 * inoput format :
 * Accept three integer as a input
 * output format:
 * print the date is "vaild " or "invaild"
 * constraints :
 * 1 <= INput <= 9999
 * same input 1 :
 * 29 02 1998
 * invaild
 * 
 * 
 * 
 * import java.util.Scanner;
 * 
 * public class fiveMay {
 * public static void main(String[] args) {
 * Scanner scanner = new Scanner(System.in);
 * System.out.print("Enter date (dd mm yyyy): ");
 * int day = scanner.nextInt();
 * int month = scanner.nextInt();
 * int year = scanner.nextInt();
 * 
 * boolean Valid = true;
 * 
 * if (year < 1900 || year > 9999) {
 * Valid = false;
 * } else if (month < 1 || month > 12) {
 * Valid = false;
 * } else if (day < 1 || day > 31) {
 * Valid = false;
 * } else if (month == 2) {
 * if (isLeapYear(year)) {
 * if (day > 29) {
 * Valid = false;
 * }
 * } else {
 * if (day > 28) {
 * Valid = false;
 * }
 * }
 * } else if ((month == 4 || month == 6 || month == 9 || month == 11) && day >
 * 30) {
 * Valid = false;
 * }
 * 
 * System.out.println(Valid ? "valid" : "not valid");
 * }
 * 
 * public static boolean isLeapYear(int year) {
 * return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
 * }
 * }
 * 
 */

/*
 * to check the wheter the given time is vaild or not
 * 
 * input :
 * Accept three integer as a input
 * output :
 * print thr timme is "vaild " or "not vaild"
 * constraint :
 * 0<= INPUT <= 10^15
 */

/*
 * give the date , write a program to calculate the numner of days in completed
 * in that year.
 * input format :
 * Accept day_num, month and yar as space separated
 * output format :
 * Display the number of completed days
 * constraints :
 * 1 <= day_num <= 31
 * 1 <= month <= 12
 * 1900 <= yy <= 9999
 * note : no need to vaildate date, assume the input will always br a vaild date
 * input :
 * 15 02 1998
 * output :
 * 45
 * 
 * 
 * 
 * import java.util.Scanner;
 * 
 * public class Main {
 * public static void main(String[] args) {
 * Scanner scanner = new Scanner(System.in);
 * 
 * System.out.print("Enter date (dd mm yyyy): ");
 * int day = scanner.nextInt();
 * int month = scanner.nextInt();
 * int year = scanner.nextInt();
 * 
 * int node = 0;
 * 
 * switch (month - 1) {
 * case 11: node += 30;
 * case 10: node += 31;
 * case 9: node += 30;
 * case 8: node += 31;
 * case 7: node += 31;
 * case 6: node += 30;
 * case 5: node += 31;
 * case 4: node += 30;
 * case 3: node += 31;
 * case 2:
 * if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
 * node += 29;
 * } else {
 * node += 28;
 * }
 * 
 * case 1: node += 31;
 * case 0: break;
 * }
 * 
 * node += day;
 * System.out.println("Completed days: " + node);
 * 
 * scanner.close();
 * }
 * }
 */

/*
 * Given 3 intenger values , arranges those value in ascending order
 * given an integer num. repeatedly add all its digits until the result has only
 * one digit and return it.
 * input format :
 * num =38
 * output :
 * 2
 * explatio :
 * process 38 -> 3 + 8 = 11 -> 1 + 1 = 2
 * since 2 has only one digit return it
 * example 2:
 * input : 0
 * output : 0
 */

/*
 * accept an integer N and print the susm if first N odd numbers
 * 
 * input : 2
 * output : 4
 * 
 * input : 5
 * output : 25
 * 
 */

/*
 * find the whether the given number is power of 2 or not
 * input 32
 * output : yes
 * 
 * input 24
 * output : no
 */

/*
 * find min max, sum and average of given n sumber without sung array.
 * note : -1 will be the terminator of the input.
 * 
 * input : 1 2 3 4 5 -1
 * output :
 * min : 1
 * max : 5
 * sum : 15
 * avg : 3
 * 
 * 
 * import java.util.*;
 * 
 * public class Main {
 * public static void main(String[] args) {
 * Scanner sc = new Scanner(System.in);
 * int num = sc.nextInt();
 * int min = num;
 * int max = num;
 * int sum = 0;
 * int count = 0;
 * 
 * while (num != -1) {
 * sum += num;
 * count++;
 * 
 * if (num < min) min = num;
 * if (num > max) max = num;
 * 
 * num = sc.nextInt();
 * }
 * 
 * if (count > 0) {
 * System.out.println("min : " + min);
 * System.out.println("max : " + max);
 * System.out.println("sum : " + sum);
 * System.out.println("avg : " + (sum / count));
 * } else {
 * System.out.println("No valid input.");
 * }
 * 
 * sc.close();
 * }
 * }
 * 
 */

/*
 * Given a N, write program to generate aseries of N values that has 2 and 3
 * power alterntivly
 * input format : b
 * accept an integer as input
 * out format :
 * print frist n element of series as output as space separated.
 * constraints :
 * 1 <= N <= 10^5
 * input : 6
 * output : 1 1 2 3 4 9
 * 
 * import java.util.*;
 * public class Main
 * {
 * public static void main(String[] args) {
 * Scanner sc = new Scanner(System.in);
 * int num = sc.nextInt(); //2
 * int two=1,three=1;
 * for(int itr=1;itr<=num;itr+=2)//
 * {
 * System.out.print(two+" ");
 * two*=2;
 * 
 * if(itr<num)
 * {
 * System.out.print(three+" ");
 * three*=3;
 * }
 * }
 * }
 * }
 * 
 * 
 * 
 * 
 * 
 * /*
 * int min = num,max=num ,sum=0,count=0;
 * while(num!=-1)
 * {
 * if(num<min)
 * {
 * min = num;
 * }
 * if(num>max)
 * {
 * max = num;
 * }
 * sum +=num;
 * count++;
 * num = sc.nextInt();
 * }
 * double avg = sum/ count;
 * System.out.println("min:"+min);
 * System.out.println("max:"+max);
 * System.out.println("sum:"+sum);
 * System.out.println("avg:"+avg);
 * 
 * int flag = 0;
 * for(int itr=1;itr<=num;itr*=2)
 * {
 * if(itr==num)
 * {
 * flag = 1;
 * }
 * }
 * if(flag == 1)
 * {
 * System.out.println("yes");
 * }
 * else
 * {
 * System.out.println("no");
 * }
 * int flag =0;
 * if(num%2!=0)
 * {
 * System.out.println("no");
 * }
 * else
 * {
 * 
 * while(num>=2)
 * {
 * num = num/2;
 * if(num%2==1)
 * {
 * flag = 1;
 * }
 * }
 * if(flag==0)
 * {
 * System.out.println("yes");
 * }
 * else
 * {
 * System.out.println("no");
 * }
 * }
 * ENTRY CHECK -> WHILE,FOR
 * 
 * EXIT CHECK -> DO WHILE
 * 
 * while(condition)
 * {
 * statement;
 * }
 * 1 2 4
 * for(initialization;condition;updation) -> increment , decrement
 * {
 * statememt; 3
 * }
 * 
 * 
 * do
 * {
 * statement;
 * }while(condition)
 * 
 */

/*


 */

/* 
 
 */