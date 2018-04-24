package main

import "fmt"
import "errors"


func f1(arg int) (int, error) {
	if arg == 69 {
		return -1, errors.New("Just not 69")
	}
	return arg + 3, nil
}


type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}


func f2(arg int) (int, error) {
	if arg == 69 {
		return -1, &argError{arg, "Please"}
	}
	return arg - 8, nil
}


func main() {

	// Builtin
	for _, i := range []int{1, 69,  80} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed: ", e)
		} else {
			fmt.Println("f1 worked: ", r)
		}
	}

	// Custom
	for _, i := range []int{1, 69, 80} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed: ", e)
			} else {
				fmt.Println("f2 worked: ", r)
			}
	}

	// Data recovery in error handling
	fmt.Println("\n", "=== Custom error handling ===")
	_, e := f2(69)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
