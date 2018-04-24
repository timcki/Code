package main

import "fmt"

func main() {
	messages := make(chan string, 3)
	signals := make(chan bool)

	// My experiment
	// messages <- "lol"

	select {
	case msg := <-messages:
		fmt.Println("got message: ", msg)
	default:
		fmt.Println("no message")
	}

	msg := "hi"

	select {
	case messages <- msg:
		fmt.Println("sent message")
	default:
		fmt.Println("no message to send")
	}

	select {
	case msg := <- messages:
		fmt.Println("Got message: ", msg)
	case sig := <- signals:
		fmt.Println("Got signal: ", sig)
	default:
		fmt.Println("No messages nor signals")
	}
}
