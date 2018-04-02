use std::{time, hash};

#[derive(Debug)]
struct Block {
    index:      isize,
    timestamp:  time::SystemTime,
    prev_hash:  u64,
    hash:       u64,
    data:       String
}

fn main() {
    let first_block = Block {
        index: 0,
        timestamp: time::SystemTime::now(),
        prev_hash: 0,
        hash: 1,
        data: String::from("First block")
    };
    println!("{:?}", first_block);
}
