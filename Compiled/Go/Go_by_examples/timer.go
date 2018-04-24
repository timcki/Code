package main

import "fmt"
import "time"

func main() {
	t1 := time.NewTimer(2 * time.Second)
	<- t1.C
	fmt.Println("Timer 1 expired")

	t2 := time.NewTimer(1 * time.Second)
	go func() {
		<-t2.C
		fmt.Println("Timer 2 expired")
	}()
	stop := t2.Stop()
	if stop {
		fmt.Println("Timer 2 stopped")
	}
}
