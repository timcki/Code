package main

import "fmt"

func main() {
	s := make([]string, 3)
	fmt.Println("s: ", s)

	s[0] = "A"
	s[1] = "Z"
	s[2] = "K"
	fmt.Println("set: ", s)
	fmt.Println("set[1]: ", s[1])

	fmt.Println("len(set): ", len(s))

	// Copy here? 
	// Yes there is a copy here. It makes sense because it has to reallocate
	// the space necessary for a larger slice.
	s = append(s, "d")
	s = append(s, "e", "f")

	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("copied: ", c)

	//My testing

	//Will this work?
	// It works. Same as before it reallocates, so might as well give it a new
	// variable.
	c1 := make([]string, len(s)+1)
	c1 = append(s, "g")

	fmt.Println("mytest: ", c1)

	l := s[3:5]
	fmt.Println("sliced: ", l)

	//So a string is not an array like it would seem from the def. OK
	t := []string{"g", "h", "longer phrase"}
	fmt.Println("test: ", t)

	//Basic stuff
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)

}
