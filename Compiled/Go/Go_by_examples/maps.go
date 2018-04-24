package main

import "fmt"

func main() {

	m := make(map[string]int)

	m["k1"] = 7
	m["key2"] = 21

	fmt.Println("map: ", m)

	v1 := m["k1"]
	fmt.Println("var1: ", v1)

	fmt.Println("len: ", len(m))

	delete(m, "key2")
	fmt.Println("map: ", m)

	_, prs := m["key2"]
	fmt.Println("is present: ", prs)

	n := map[string]int{"foo": 1, "bar": 23}
	fmt.Println("map: ", n)
}
