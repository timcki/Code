package main

import "fmt"

type person struct {
	name string
	age  int
}

// Really like the language so far. It's like a newer version of C, which
// I dig a lot.
func main() {
	fmt.Println(person{"Bob", 20})

	fmt.Println(person{name: "Alice", age: 23})

	fmt.Println(person{name: "Fred"})

	s := person{"Sean", 50}
	fmt.Println(s.name)

	sp := &s

	sp.age = 61
	fmt.Println(s)
}
