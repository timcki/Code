package main

import "fmt"

func zeroval(ival int) {
	ival = 0
}

func zeroptr (ival *int) {
	*ival = 0
}

// Exactly like in C. Nice.
func main() {
	value := 20
	fmt.Println("value: ", value)

	zeroval(value)
	fmt.Println("value: ", value)

	zeroptr(&value)
	fmt.Println("value: ", value)

	fmt.Println("pointer: ", &value)
}
