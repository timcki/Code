use std::io::stdin;

macro_rules! scan {
    ( $string:expr, $sep:expr, $( $x:ty ),+ ) => {{
        let mut iter = $string.split($sep);
        ($(iter.next().and_then(|word| word.parse::<$x>().ok()),)*)
    }}
}

struct Triplet(i16, i16, i16);

impl Triplet {
    fn new(x: i16, y: i16, z: i16) -> Triplet {
        Triplet(x, y, z)
    }

    fn into_array(self) -> [i16; 3] { [self.0, self.1, self.2] }
}

fn main() {

    let mut bob_str = String::new();
    let mut alice_str = String::new();

    stdin().read_line(&mut alice_str).unwrap();
    stdin().read_line(&mut bob_str).unwrap();

    let bob = scan!(bob_str, char::is_whitespace, i16, i16, i16);
    let alice = scan!(alice_str, char::is_whitespace, i16, i16, i16);

    let bob_t = Triplet::new(bob.0.unwrap(), bob.1.unwrap(), bob.2.unwrap());
    let alice_t = Triplet::new(alice.0.unwrap(), alice.1.unwrap(), alice.2.unwrap());

    let mut bob_v: i8 = 0;
    let mut alice_v: i8 = 0;

    for it in bob_t.into_array().iter().zip(alice_t.into_array().iter()) {
            if it.0 > it.1 { bob_v += 1; }
            else if it.0 < it.1 { alice_v += 1; }

    }
    println!("{} {}", alice_v, bob_v);

}