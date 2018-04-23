package main

import "fmt"

type Point struct {
	x int
	y int
}

type Rect struct {
	p1 Point
	p2 Point
}

func (r *Rect) width() int {
	width := r.p1.x - r.p2.x
	if width < 0 {
		width *= -1
	}
	return width
}

func (r *Rect) height() int {
	height := r.p1.y - r.p2.y

	if height < 0 {
		height *= -1
	}
	return height
}

func (r *Rect) area() int {

	return r.width() * r.height()

}


func (r Rect) perim() int {

	return 2*(r.width() + r.height())

}

func main() {
	r := Rect{p1: Point{2, 3}, p2: Point{5, 8}}

	fmt.Println("area: ", r.area())
	fmt.Println("perim: ", r.perim())

	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim: ", rp.perim())
}
