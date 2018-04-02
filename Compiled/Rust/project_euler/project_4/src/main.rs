fn is_palindrome(num: &[u8]) -> bool {
    let length = num.len();
    true
}

fn main() {
    'outer: for x in (100u32..1000u32).rev() {
        for y in (100u32..1000u32).rev() {
            let number_checked::&[u8] = (x*y).to_owned();
            if is_palindrome(&number_checked) { println!("{}", number_checked); break 'outer; }
        }
    }
}
