
import java.util.Scanner;

public class Game {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\n\t\t\t *** NUMBER GAME *** \n\t\t\t(Made By Abdul Wasay)\n");
        String str1;
        String strLower;
        do {
            System.out.println("Think of any numbers, as many as you want (Different Numbers are Preferred) Range[1, 2, 3, 4, 50-9]. (E.g: )\n");
            System.out.println("Except the case (99999)");
            System.out.println("\nHow many numbers are there?");
            int noOfNOs = sc.nextInt();

            System.out.println("If you have thought of the numbers, please type 'Yes/y' (Y/N): \n");
            String yes = sc.next();

            String lower = yes.toLowerCase(); // converting to lowercase

            if (lower.equals("yes") || lower.equals("y")) {
                System.out.println("\nNow, add all the numbers together. (E.g: 1+2+3+4+5=15) \n");
                System.out.println("If you want to proceed, please type 'Yes/y' (Y/N): \n");
                yes = sc.next();

                lower = yes.toLowerCase();

                if (lower.equals("yes") || lower.equals("y")) {
                    System.out.println("Now, subtract the number that resulted from the addition\n" +
                            " by considering the numbers you initially selected as a single number. (E.g: 12345-15 = 12,330)");

                    System.out.println("""
                          Now, remember the value that resulted from the subtraction.
                          Hide any one digit from that value, and then enter the remaining digits one by one.
                          (E.g: Value = 12330.... now HIDE any digit for this example,\s
                          let's say we HIDE 2 and Enter remaining Digits (one by one) 1, 3, 3, 0):""");

                    System.out.println("\n\n\t*** Enter Digits (ONE BY ONE) *** ");
                    int[] numbers = new int[noOfNOs - 1];

                    for (int i = 0; i < noOfNOs - 1; i++) {
                        System.out.println("Enter Number " + (i + 1) + " : ");
                        numbers[i] = sc.nextInt();
                    }

                    System.out.println("\n*** Thank you for Entering the remaining digits...");
                    System.out.println("\n\t\t*** Now the machine is guessing the number that you hid before ***");
                    int sum = 0;
                    for (int j = 0; j < noOfNOs - 1; j++) {
                        sum = numbers[j] + sum;
                    }


                    int ans;
                    if (sum < 9) {
                        ans = 9 - sum;
                        System.out.println("The Number You Hid is : " + ans);
                    } else {
                        String str = String.valueOf(sum);
                        int length = str.length();
                        int[] break_Nos = new int[length];

                        for (int i = 0; i < length; i++) {
                            break_Nos[i] = Character.getNumericValue(str.charAt(i)); // Convert char to int and store in array
                        }

                        int sum_breakNos = 0;
                        for (int j = 0; j < length; j++) {
                            sum_breakNos = break_Nos[j] + sum_breakNos;
                        }

                        ans = 9 - sum_breakNos;
                        System.out.println("The Number You Hid is : " + ans);
                    }


                } else {
                    System.out.println("\n\t\t\t*** GAME ENDED ***");
                }


            } else {
                System.out.println("\n\t\t\t*** GAME ENDED ***");
            }

            System.out.println("\nDo you want to Play again? (y/n)\n");
            str1 = sc.next();

            strLower = str1.toLowerCase();
        }while (strLower.equals("yes") || strLower.equals("y") || strLower.equals("ys"));
        System.out.println("THANK YOU FOR PLAYING THE 'NUMBER GAME' MADE BY ABDUL WASAY ");
    }
}


