use std::thread::sleep;
use std::time::Duration;

fn generate_primes(low_num: usize) -> usize {
    (low_num+1..).filter(|&x| (2..x).all(|y| x % y != 0) ).take(1).last().unwrap()
}


fn main() {
    let mut prime: usize = 2;
    let mut tmp: usize = 2;
    let mut the_number: usize = 600851475143;

    while the_number != 1 {
        if the_number % prime == 0 { the_number = the_number / prime; }
        else {
            tmp = prime;
            prime = generate_primes(tmp);
        }
        println!("{}", the_number);
    }
}
