package main

import "fmt"


// Pretty expected so far
func plus(a int, b int) int {
	return a + b
}

func plusPlus(a, b, c int) int {
	return a + b + c
}

// Multiple return values
func vals() (int, int) {
	return 4, 5
}

//Variadic functions
func sum(nums ...int) int {
	fmt.Print(nums, " ")
	fmt.Print("\n")
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}

func main() {
	res := plus(1, 2)
	fmt.Println("plus result: ", res, "\n")

	res = plusPlus(1, 2, 3)
	fmt.Println("plusPlus result: ", res, "\n")

	a, b := vals()
	fmt.Println("multiple values: ", a, b, "\n")

	//Conventional
	total := sum(1, 2, 3, 4, 5, 6)
	fmt.Println("total: ", total, "\n")

	// Passing a slice. Important to remember about the three dots
	nums := []int{1, 2, 3, 4}
	total = sum(nums...)
	fmt.Println("total with slice: ", total)
}
