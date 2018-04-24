package main

import "fmt"
import "time"

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println(id, " --> started job  --", j)
		time.Sleep(time.Second)
		fmt.Println(id, " --> finished job --", j)
		fmt.Println(id, "!! sending result", j * 4)
		results <- j * 4
	}
}

func main() {
	jobs := make(chan int, 10)
	results := make(chan int, 10)


	for id := 0; id < 4; id++ {
		go worker(id, jobs, results)
	}

	for job := 1; job < 20; job++ {
		jobs <- job
	}

	close(jobs)

	var sum int
	for i := 0; i < 20; i++ {
		select{
		case num := <-results:
			sum += num
		case <- time.After(2 * time.Second):
			continue
		}
	}
	fmt.Println("Sum:", sum)
}
