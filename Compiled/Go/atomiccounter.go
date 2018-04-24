package main

import "time"
import "fmt"
import "sync/atomic"

func main() {
	var ops uint64

	for i := 0; i < 50; i++ {
		go func() {
			for {
				atomic.AddUint64(&ops, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}
	time.Sleep(time.Second)
	final := atomic.LoadUint64(&ops)
	fmt.Println("ops:", final)
}
