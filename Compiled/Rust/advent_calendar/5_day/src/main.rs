extern crate crypto;
extern crate num_cpus;

use crypto::digest::Digest;
use crypto::md5::Md5;

use std::thread;
use std::sync::{Arc, Mutex};
use std::sync::atomic::{AtomicUsize, Ordering}

const PREFIX: &'static str = "reyedfim"
const PREFIX_LEN: usize = 8;
const MASK_SECOND_NIBBLE: u8 = 255 ^ (16 + 32 + 64 + 128);

fn to_char(num: u8) -> char {if num < 10 { ( num + 48 ) as char} else { (num + 87) as char } }

fn contains_five_zeroes(x: u8, y: u8, z: u8) -> bool { x | y | (z >> 4) == 0 }

fn main() {
    println!("Lemao");
}
