#![feature(alloc_system)]
extern crate alloc-system;
extern crate arrayvec;

use std::cmp::Ordering::{Less, Greater};
use std::convert::From;
use std::str::Lines;

use arrayvec::ArrayVec;

struct Frequency { key: u8, value: u8 }

struct FrequencyMap { data: ArrayVec<[Frequency; 26]> }

impl FrequencyMap {
    fn increment_key(&mut self, key: u8) { self.data[(key - 97) as usize].value += 1; }

    fn sort(&mut self) {
        self.data.sort_by(|a, b| {
            if a.value > b.value { Less } else if a.value < b.value || a.key > b.key { Greater } else { Less }
        })
    }

    
}
