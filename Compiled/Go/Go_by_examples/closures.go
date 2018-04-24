package main

import "fmt"

// func() int so it returns a closure
func intSequence() func() int {
	i := 0
	// Return a closure
	return func() int {
		i++
		return i
	}
}

func main() {

	nextInt := intSequence()

	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	newInts := intSequence()
	fmt.Println(newInts())
}
