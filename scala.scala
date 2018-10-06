/*
  This program won't run properly without an input.
  Try with: abc
*/
object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello World from Scala!")
    println(scala.io.StdIn.readLine())
  }
}
