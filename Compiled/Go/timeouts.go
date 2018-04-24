package main

import "time"
import "fmt"

func main() {
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	select {
		case res := <-c1:
			fmt.Println(res)
		case <- time.After(1 * time.Second):
			fmt.Println("timeout 1")
	}

	c2 := make(chan string, 1)
	// I noticed that if I use c1 here, insted of creating a new one
	// only the first message go through, even if I set a buffer of 2 on the
	// channel. I guess it's because of only one select.

	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()


	select {
		case res := <- c2:
			fmt.Println(res)
		case <- time.After(4 * time.Second):
			fmt.Println("timeout 2")
	}
}
