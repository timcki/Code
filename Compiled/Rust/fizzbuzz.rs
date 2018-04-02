
#[derive(Debug)]
enum FizzBuzzType {
    Fizz,
    Buzz,
    FizzBuzz,
    Value(u64)
}

fn main() {
    	for x in (1..101).map(to_fzbz) {
    	    match x {
    	        FizzBuzzType::Value(x) => println!("{:?}", x),
    	        _ => println!("{:?}", x)
    	    }
    	}
    }

fn to_fzbz(x: u64) -> FizzBuzzType {
	match x {
		x if x % 15 == 0 => FizzBuzzType::FizzBuzz,
		x if x % 3 == 0 => FizzBuzzType::Fizz,
		x if x % 5 == 0 => FizzBuzzType::Buzz,
		x => FizzBuzzType::Value(x)
	}
}