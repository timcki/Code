package main

import "time"
import "fmt"

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			j, more := <-jobs
			// More realistic with this
			time.Sleep(1 * time.Second)
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("All jobs received")
				done <- true
				return
			}
		}
	}()

	for i := 1; i < 5; i++ {
		jobs <- i
		fmt.Println("Sent job", i)
	}
	close(jobs)

	fmt.Println("Closed jobs channel")

	<- done
}
