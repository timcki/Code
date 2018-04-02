use std::iter::empty;

struct Sieve {
    primes: Box<Iterator<Item = usize>>
}

const THE_NUMBER: usize = 600_851_475_143;

impl Sieve {
    
    fn init(max: usize) -> Box<Iterator<Item = usize>> {
        if max < 2 { return Box::new(empty()) }
        
        let mut bool_primes = vec![true; max+1];
        let sqrmax = (max as f64).sqrt() as usize;
        bool_primes[0] = false;
        println!("{}", sqrmax);

        for x in 2..sqrmax {
            if bool_primes[x] {
                let mut tmp = x*x;
                while tmp <= max {
                    bool_primes[tmp] = false;
                    tmp += x;
                }
            }
        }

        Box::new(bool_primes.into_iter().enumerate()
                            .filter_map(|(nm, is_prm)| if is_prm { Some(nm) } else { None }))
    }
}


fn main() {
    let sieve = Sieve::init(10_000_000_000);
    println!("{:?}", sieve.collect::<Vec<usize>>());
}
