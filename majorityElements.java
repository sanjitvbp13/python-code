complete the function find majority_elements() which receives of elements and sortd array as input.


i/p: 5
1  2 2 2 2

O/p :
2 is majority element


import java.util.*;
public class Main
{
    public static void Major(int []arr,int noe)
    {
        int count=1;
        int max = noe/2;
        int itr=0;
        for(itr=0;itr<noe-1;itr++)
        {
            if(arr[itr]==arr[itr+1])
            {
                count++;
            }
            else 
            {
                if(count>max)
                {
                 break;
                }
                count=1;
            }
        }
        if(count>max)
        {
        System.out.println(arr[itr]);
        }
        else
        {
            System.out.println("No majority element");
        }
        
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int noe = sc.nextInt();
         //datatype name_arr [] = new datatype[noe];
	     int arr [] = new int[noe];
	     for(int itr = 0;itr<noe;itr++)
	     {
	         arr[itr] = sc.nextInt();
	     }
	   //  for(int itr = 0;itr<noe;itr++)
	   //  {
	   //      System.out.print(arr[itr]+" ");
	   //  }
	     Major(arr,noe);
	}
}
