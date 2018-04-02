struct Fibonnaci {
    alast: i64,
    last: i64
}

impl Iterator for Fibonnaci {
    type Item = i64;
    fn next(&mut self) -> Option<i64> {
        let sum = self.alast + self.last;
        self.alast = self.last;
        self.last = sum;
        Some(sum)
    }

}

impl Fibonnaci {
    fn new() -> Fibonnaci {
        Fibonnaci { alast: 0, last: 1 }
    }
}

fn main() {
    let fibo = Fibonnaci::new()
        .take_while(|x| x < &4000000)
        .filter(|x| x % 2 == 0)
        .fold(0, |sum, i| sum + i);
    println!("{}", fibo);
}
