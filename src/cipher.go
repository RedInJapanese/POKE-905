package main 


import (
	"fmt"
	"os"
	"bufio"
)
// an error is a built in interface type in go that returns a string with an error message
// panic() is similar to exit() in c/c++ and exists the program with the provided error message
func file_checker(e error){
	if e != nil {
		panic(e)
	}
}

func main() {
	inFile, e := os.Open("rgb.txt")
	file_checker(e)

	reader := bufio.NewReader(inFile)
	b:=make([]byte, 32)

	for {
		i, e := reader.Read(b)
		if e != nil {
			fmt.Println(e)
			break
		}
		fmt.Println(string(b[:i]))
	}
}