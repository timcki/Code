package main

import "fmt"

// A classic to be sure but a welcome one
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func main() {
	fmt.Println(factorial(7))
}
