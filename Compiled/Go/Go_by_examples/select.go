package main

import "time"
import "fmt"

func main() {

	chans := make([]chan string, 5)
	fmt.Println(chans)


	for i := 0; i < 4; i++ {
	
		go func() {
			time.Sleep(1 * time.Second)
			chans[i] <- fmt.Sprintf("done %d", i)
		}()

	}
	
	for i := 0; i < 5; i++ {
		select {

			case msg1 := <-chans[0]:
				fmt.Println("received: ", msg1)

			case msg2 := <-chans[1]:
				fmt.Println("received: ", msg2)

			case msg3 := <-chans[2]:
				fmt.Println("received: ", msg3)

			case msg4 := <-chans[3]:
				fmt.Println("received: ", msg4)

			case msg5 := <-chans[4]:
				fmt.Println("received: ", msg5)
		}
	}

}
