use std::cmp::max;
use std::str::Lines;

fn is_possible(x: u16, y: u16, z: u16) -> bool {
    let sum = x + y + z;
    let max = max( max(x, y), z);
    sum - max > max
}

struct TriangleRowIterator<'a> { triangles: Lines<'a> }

impl<'a> TriangleRowIterator<'a> {
    fn new(input: &'a str) -> TriangleRowIterator<'a> { TriangleRowIterator { triangles: input.lines() } }
}

impl<'a> Iterator for TriangleRowIterator<'a> {
    type Item = bool;
    fn next(&mut self) -> Option<bool> {
        self.triangles.next().map(|line| {
            let mut sides = line.split_whitespace().map(|x| x.parse::<u16>().unwrap());
            is_possible(sides.next().unwrap(), sides.next().unwrap(), sides.next().unwrap())
        })
    }
}

struct TriangleColumnIterator<'a> { rows: Lines<'a> }

impl<'a> TriangleColumnIterator<'a> {
    fn new(input: &'a str) -> TriangleColumnIterator<'a> { TriangleColumnIterator { rows: input.lines() } }
}

impl<'a> Iterator for TriangleColumnIterator<'a> {
    type Item = usize;
    fn next(&mut self) -> Option<usize> {
        let first_row = self.rows.next().map(|x| x.split_whitespace().map(|x| x.parse::<u16>().unwrap()));
        let second_row = self.rows.next().map(|x| x.split_whitespace().map(|x| x.parse::<u16>().unwrap()));
        let third_row = self.rows.next().map(|x| x.split_whitespace().map(|x| x.parse::<u16>().unwrap()));
        if let (Some(first), Some(second), Some(third)) = (first_row, second_row, third_row) {
            Some(first.zip(second).zip(third).filter(|&((x, y), z)| is_possible(x, y, z)).count())
        } else {
            None
        }
    }
}

fn main() {
    let input = include_str!("input.txt");
    let valid_triangles = TriangleRowIterator::new(input).filter(|&x| x).count();
    println!("{:?}", valid_triangles);
    let valid_triangles = TriangleColumnIterator::new(input).fold(0, |acc, next| acc + next);
    println!("{:?}", valid_triangles);
}

#[test]
fn part_one() {
    let input = include_str!("input.txt");
    let valid_triangles = TriangleRowIterator::new(input).filter(|&x| x).count();
    assert_eq!(862, valid_triangles);
}

#[test]
fn part_two() {
    let input = include_str!("input.txt");    
    let valid_triangles = TriangleColumnIterator::new(input).fold(0, |acc, next| acc + next);
    assert_eq!(1577, valid_triangles);
}
