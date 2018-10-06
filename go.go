package main
import "os"
import "fmt"
import "bufio"
func main() {
	fmt.Println("Hello World from Go!")
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	fmt.Print(text)
}
