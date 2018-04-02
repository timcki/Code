use std::io;

macro_rules! scanline {
    ($x:expr) => {
       io::stdin().read_line(&mut $x).unwrap();
    };
}

fn main() {
    let mut line: String = String::new();
    scanline!(line);

    let num_list: Vec<i64> = line.trim().split(" ")
        .map(|s| s.parse().expect("ASS"))
        .collect();

    let mut max: i64 = num_list.iter().sum();
    let mut min: i64 = num_list.iter().sum();

    min -= *num_list.iter().max().unwrap();
    max -= *num_list.iter().min().unwrap();

    println!("{} {}", min, max);
}
