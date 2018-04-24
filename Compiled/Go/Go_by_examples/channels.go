package main

import "fmt"

func ping(pings chan<- string, msg string) {
	pings <- msg
}

func pong(pings <-chan string, pongs chan<- string) {
	msg := <- pings
	pongs <- msg
}

func main() {

	// Normal channel
	messages := make(chan string)

	go func() { messages <- "ping\n" }()

	msg := <- messages
	fmt.Println(msg)


	// Buffered channel

	messages = make(chan string, 2)

	messages <- "buffered"
	messages <- "channel"

	fmt.Println(<-messages)
	fmt.Println(<-messages)

	// Channel directions
	pings := make(chan string)
	pongs := make(chan string)

	go ping(pings, "Message that I pass")
	go pong(pings, pongs)

	fmt.Println(<-pongs)
}
