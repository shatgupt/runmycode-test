package main
import "os"
import "fmt"
import "strings"
func main() {
	fmt.Println("Hello World from go!")
	fmt.Println(fmt.Sprintf("%v Args: [%v]", len(os.Args[1:]), strings.Join(os.Args[1:], ", ")))
}
