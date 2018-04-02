use std::collections::HashSet;
use std::io::{BufRead, BufReader, Lines};
use std::fs::File;

fn main() {

    let f = File::open("input.txt").unwrap();
    let file = BufReader::new(&f);
    let mut hashset = HashSet::with_capacity(20);
    for line in file.lines().take(5) {
        let u_line = line.unwrap();
        test_line(u_line);
        let split_words = u_line.split_whitespace();
        let inserting_result = split_words.map(|word| hashset.insert(word)).any(|result: bool| result == false);

		println!("{:?}", inserting_result);
    }
    //let lines = file.lines().take(1).map(|line| &line.unwrap().split(" ").collect::<Vec<&str>>());
    /*
    for line in file.lines().take(5). {
        let mut hashset: HashSet<&str> = HashSet::new();
        let words = line.split(" ");
        words.map(|x| hashset.insert(&x)).collect::<Vec<bool>>();
    }
    */
    let mut hashset: HashSet<&str> = HashSet::new();
    let _ = hashset.insert(&"First string");
    println!("{:?}", hashset);
    if !(hashset.insert("First string")) { println!("33"); }
}

fn test_line(line: <Lines>) -> bool {
    false
}
