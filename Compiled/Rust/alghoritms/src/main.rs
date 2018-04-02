use std::io;

fn main() {
    let mut size = String::new();
    let mut line = String::new();
    io::stdin().read_line(&mut size).unwrap();
    io::stdin().read_line(&mut line).unwrap();

    let sum_v: Vec<i32> = line.trim().split(" ")
        .map(|s| s.parse().unwrap())
        .collect();

    let mut x: i32 = 0;

    for fuck in sum_v.iter() { x += *fuck; }

    println!("{}", x);

}