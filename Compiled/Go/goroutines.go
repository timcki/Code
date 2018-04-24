package main

import "fmt"

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {
	f("direct")

	go f("goroutine")


	go func(from string) {
		fmt.Println(from)
	}("going")

	// Running this thing in an goroutine is a bad idea
	fmt.Scanln()
	fmt.Println("done")
}
