#[derive(Clone, Copy)]
enum MarchDirection {
    North,
    East,
    South,
    West,
}
#[derive(Debug, PartialEq, Clone)]
struct Location {
    x: i32,
    y: i32
}

/*
impl PartialEq for Location {
    fn eq(&self, other: &Location) -> bool {
        &self.x == &other.x && &self.y == &other.y
    }
}
*/

use MarchDirection::*;


fn main() {
    let tmp = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5".to_string();
    let mut location = Location { x: 0 , y: 0 };
    let mut cur_dir = North;
    let mut commands: Vec<(&str, i32)> = Vec::new();
    let mut visited: Vec<Location> = Vec::new();
    let mut first_time = Location { x: 0, y: 0 };
    for s in tmp.split(", ") {
        let num: i32 = s[1..s.len()].parse().unwrap();
        let dir: &str = &s[0..1];
        commands.push((dir, num));
    }

    for tup in commands.into_iter() {
        visited.push(location.clone());
        match (cur_dir, tup) {
            (North, ("L", x)) =>    { location.x -= x; cur_dir = West; },
            (North, ("R", x)) =>    { location.x += x; cur_dir = East; },

            (East, ("L", x)) =>     { location.y += x; cur_dir = North; },
            (East, ("R", x)) =>     { location.y -= x; cur_dir = South; },

            (South, ("L", x)) =>    { location.x += x; cur_dir = East; },
            (South, ("R", x)) =>    { location.x -= x; cur_dir = West; },

            (West, ("L", x)) =>     { location.y -= x; cur_dir = South; },
            (West, ("R", x)) =>     { location.y += x; cur_dir = North; },

            _ => {}
        }
        println!("After assert: {:?}\n\n", location);
        if location.x.abs() + location.y.abs() == 154 { println!("TYISONE:\t{:?}", location); };
        if visited.contains(&location) { first_time = location.clone(); }
    }
    println!("{:?}", visited);
    println!("First time: {:?}\nHorizontal: {}\tVertical: {}", first_time, location.x, location.y);
}