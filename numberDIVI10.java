import java.util.Scanner;

public class numberDIVI10 {
    public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
        long num = sc.Scanner(system.in);
        long pow = 1;
        while(pow<num)
        {
            int dig = (int)(num/pow)%10);
            System.out.println(dig,"");
            pow(+10)
        }
	}
}

/*
 * 12345/1= 12345%10=12345
 * 12345/10=124%10=4
 * 12345/100= 123%10=3
 * 12345/1000=12%10=2
 * 12345/10000=1%10=1
 */
