package main

import "fmt"

func main() {
	nums := []int{2, 3, 4}
	sum := 0
	// Ranges are pretty cozy. I like the idea and execution
	// I guess it should give the position and the item
	// It does
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	for i, num := range nums {
		if num == 3 {
			fmt.Println("index: ", i)
		}
	}

	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	for k := range kvs {
		fmt.Println("keys: ", k)
	}

	// You can iterate over a unicode string
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
