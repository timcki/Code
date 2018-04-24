package main

import "fmt"
import "time"

func main() {
	ticker := time.NewTicker(500 * time.Millisecond)

	go func() {
		for tick := range ticker.C {
			fmt.Println("Tick at", tick)
		}
	}()

	time.Sleep(3 * time.Second)
	ticker.Stop()
	fmt.Println("Ticker stopped")
}
