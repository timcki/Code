package main

import "time"
import "fmt"

// what
func main() {
	// producing requests
	// We are making 2 separate request handling methods
	// First
	requests := make(chan int, 5)
	for i := 1; i <=5; i++ {
		requests <- i
	}
	close(requests)

	limiter := time.Tick(200 * time.Millisecond)

	// Here we just tick statically every 200 ms and we gud
	for r := range requests {
		<-limiter
		fmt.Println("request", r, time.Now())
	}


	// Allows up to 3 requests at the same time, and then handles them every 200 ms
	burstyLimiter := make(chan time.Time, 3)


	go func() {
		// I can move the for here without any problem. Makes the code more readable
		// Here we're allowing 3 at the same time, and then we're just spamming a
		// request allow every 200 ms
		
		for i := 0; i < 3; i++ {
			burstyLimiter <- time.Now()
		}
		// Modified the code to allow 3 at a time every 200 ms
		for t := range time.Tick(200 * time.Millisecond) {
			burstyLimiter <- t
			burstyLimiter <- t
			burstyLimiter <- t
		}
	}()

	burstyRequests := make(chan int, 10)

	for i := 1; i <= 10; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)
	for r := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request:", r, time.Now())
	}
}
