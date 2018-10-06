/*
  This program won't run properly without an input.
  Try with: abc
*/
import java.util.Scanner;

class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello World from Java!");
    Scanner scan = new Scanner(System.in);
    System.out.println(scan.nextLine());
  }
}
