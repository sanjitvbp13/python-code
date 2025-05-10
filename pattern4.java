* * * * * 
 *    * 
  *  *
   *
   

   public class Main {
    public static void main(String[] args) {
        int n = 4; 

        for (int i = 0; i < n; i++) {
            
            for (int space = 0; space < i; space++) {
                System.out.print(" ");
            }

            int stars = n - i;
            for (int j = 0; j < stars; j++) {
                
                if (i == 0 || j == 0 || j == stars - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }

                
                if (j < stars - 1) {
                    System.out.print(" ");
                }
            }

            System.out.println();
        }
    }
}
