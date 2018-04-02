#[derive(Debug)]
struct Memory {
    table: [[i32; 19]; 19]
}

impl Memory {
    fn new() -> Memory {
        Memory { table: [[0;19];19] }
    }

    fn add_number(&mut self, pos: (usize, usize), num: i32) {
        self.table[pos.0][pos.1] = num;
    }
    fn pretty_print(&self) {
        for x in self.table.iter() {
            for y in x.iter() {
                print!("{:>9}",  y);
            }
            println!();
        }
    }

}


fn main() {
    let mut memory = Memory::new();
    // Init the mem with 1 in the middle and start doing magic
    let mut x = 9;
    let mut y = 9;
    let mut count = 1;
    memory.add_number((y, x), 1);

    while x < 14 {
        if count % 2 == 1 {
            for _ in 0..count {
                x += 1;
                let row_up = &memory.table[y-1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_lev = &memory.table[y][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_dow = &memory.table[y+1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                memory.add_number((y, x), row_up+row_lev+row_dow);
            }
            for _ in 0..count {
                y -= 1;
                let row_up = &memory.table[y-1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_lev = &memory.table[y][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_dow = &memory.table[y+1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                memory.add_number((y, x), row_up+row_lev+row_dow);
            }
        }
        else {
            for _ in 0..count {
                x -= 1;
                let row_up = &memory.table[y-1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_lev = &memory.table[y][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_dow = &memory.table[y+1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                memory.add_number((y, x), row_up+row_lev+row_dow);
            }
            for _ in 0..count {
                y += 1;
                let row_up = &memory.table[y-1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_lev = &memory.table[y][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                let row_dow = &memory.table[y+1][x-1..x+2].iter().fold(0, |acc, sum| acc + sum);
                memory.add_number((y, x), row_up+row_lev+row_dow);
            }
        }
        count += 1;
    }

    memory.pretty_print();
}
