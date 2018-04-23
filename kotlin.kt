fun main(args: Array<String>) {
  println("Hello World from kotlin!")
  println("${args.size} Args: " + args.joinToString(prefix = "[", postfix = "]"))
}
