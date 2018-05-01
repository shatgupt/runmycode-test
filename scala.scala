object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello World from scala!")
    println(s"${args.length} Args: " + args.mkString("[", ", ", "]"))
  }
}
